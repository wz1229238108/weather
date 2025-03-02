import pymysql
import requests
import json

# 数据库连接配置
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "123456",
    "database": "tianqi",
}

# 读取中国城市编码数据
def read_china_city_codes():
    with open("china.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

# 爬取当前天气数据
def crawl_current_weather(city_id):
    base_url = "https://devapi.qweather.com/v7/weather/now"
    key = ""

    full_url = f"{base_url}?location={city_id}&key={key}"

    try:
        response = requests.get(full_url)
        data = response.json()

        if data["code"] == "200":
            return data["now"]
        else:
            print(f"Error: {data['code']}, {data['message']}")
            return None

    except Exception as e:
        print(f"Error: {e}")
        return None

# 将当前天气数据保存到数据库
def save_current_weather_to_database(city_name, current_weather_data):
    try:
        connection = pymysql.connect(**db_config)
        cursor = connection.cursor()

        sql = '''
            INSERT INTO weatherdata (
                城市, 时间, 温度, 体感温度, 天气情况, 
                风力等级, 湿度, 能见度
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        '''
        values = (
            city_name,
            current_weather_data["obsTime"],
            current_weather_data["temp"],
            current_weather_data["feelsLike"],
            current_weather_data["text"],
            current_weather_data["windScale"],
            current_weather_data["humidity"],
            current_weather_data["vis"],
        )
        cursor.execute(sql, values)

        connection.commit()
        print(f"当前天气数据保存成功: {city_name}")

    except pymysql.Error as err:
        print(f"数据库错误: {err}")

    finally:
        if connection:
            cursor.close()
            connection.close()

if __name__ == "__main__":
    # 读取中国城市编码数据
    china_city_codes = read_china_city_codes()

    if china_city_codes:
        for city_name, city_id in china_city_codes.items():
            # 获取当前天气信息
            current_weather_data = crawl_current_weather(city_id)

            if current_weather_data:
                # 将当前天气数据保存到数据库
                save_current_weather_to_database(city_name, current_weather_data)
