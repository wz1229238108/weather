from pymysql import connect


def create_connection():
    return connect(host='localhost', user='root', password='123456', database='tianqi', port=3306, charset='utf8')


def city_tem(data):
    conn = None
    cursor = None
    try:
        conn = create_connection()
        cursor = conn.cursor()
        if data == '温度':
            cursor.execute("SELECT 城市, 温度, 体感温度, 天气情况, 风力等级, 湿度, 能见度 FROM weatherdata")
        elif data == '体感温度':
            cursor.execute(
                "SELECT 城市, 温度, 体感温度, 天气情况, 风力等级, 湿度, 能见度 FROM weatherdata")
        elif data == '风力等级':
            cursor.execute(
                "SELECT 城市, 温度, 体感温度, 天气情况, 风力等级, 湿度, 能见度 FROM weatherdata")
        elif data == '湿度':
            cursor.execute(
                "SELECT 城市, 温度, 体感温度, 天气情况, 风力等级, 湿度, 能见度 FROM weatherdata")
        else:
            cursor.execute(
                "SELECT 城市, 温度, 体感温度, 天气情况, 风力等级, 湿度, 能见度 FROM weatherdata")
        # 扩展查询以包括更多天气相关的数据


        # 获取查询结果
        city_weather_data = cursor.fetchall()

        # 手动创建省份城市的列表
        province_cities = {
            '北京': '北京',
            '天津': '天津',
            '河北': '石家庄',
            '山西': '太原',
            '内蒙古': '呼和浩特',
            '辽宁': '沈阳',
            '吉林': '长春',
            '黑龙江': '哈尔滨',
            '上海': '上海',
            '江苏': '南京',
            '浙江': '杭州',
            '安徽': '合肥',
            '福建': '福州',
            '江西': '南昌',
            '山东': '济南',
            '河南': '郑州',
            '湖北': '武汉',
            '湖南': '长沙',
            '广东': '广州',
            '广西': '南宁',
            '海南': '海口',
            '重庆': '重庆',
            '四川': '成都',
            '贵州': '贵阳',
            '云南': '昆明',
            '西藏': '拉萨',
            '陕西': '西安',
            '甘肃': '兰州',
            '青海': '西宁',
            '宁夏': '银川',
            '新疆': '乌鲁木齐',
            '台湾': '台北',
            '香港': '香港',
            '澳门': '澳门',
        }

        # 创建空字典来存放省份的天气数据
        province_weather_data = {}

        # 将天气数据赋值给对应的省份
        for province, cities in province_cities.items():
            for city_data in city_weather_data:
                city = city_data[0]
                if city in cities:
                    province_weather_data[province] = {
                        '温度': city_data[1],
                        '体感温度': city_data[2],
                        '天气情况': city_data[3],
                        '风力等级': city_data[4],
                        '湿度': city_data[5],
                        '能见度': city_data[6]
                    }
                    break

        # 返回按省份组织的天气数据
        return province_weather_data
    except Exception as e:
        print("查询错误:", e)
        return None
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


# 示例用法：获取所有城市的天气数据
province_weather_data = city_tem(data='温度')
print(province_weather_data)
