from .utils import *

def highest_wind_humidity():
    try:
        # 查询风速最高的十个城市和对应的风速
        cursor.execute("SELECT 城市, 风力等级 FROM weatherdata ORDER BY 风力等级 DESC LIMIT 10")
        highest_wind = cursor.fetchall()

        # 查询湿度最高的十个城市和对应的湿度
        cursor.execute("SELECT 城市, 湿度 FROM weatherdata ORDER BY 湿度 DESC LIMIT 10")
        highest_humidity = cursor.fetchall()

    except Exception as e:
        print("查询错误:", e)
        return None

    return highest_wind, highest_humidity


def highest_wind_weather():
    try:
        # 查询风速最高的十个城市和对应的风速
        tables02_sql = '''

                                select 天气,count(1) num
                                from lishiweathers
                                group by 天气
                                order by num desc
                                limit 10
                               

        '''
        tables03_sql = '''

                                        select 风向,count(1) num
                                        from lishiweathers
                                        group by 风向
                                        order by num desc
                                        limit 10
                                        

                '''
        cursor.execute(tables02_sql)
        # cursor.execute("SELECT 城市, 天气 FROM lishiweathers ORDER BY 天气 DESC LIMIT 10")
        highest_wind = cursor.fetchall()
        cursor.execute(tables03_sql)
        # 查询湿度最高的十个城市和对应的湿度
        # cursor.execute("SELECT 城市, 风向 FROM lishiweathers ORDER BY 风向 DESC LIMIT 10")
        highest_humidity = cursor.fetchall()



        print("highest_wind=",highest_wind)
        print("highest_humidity=", highest_humidity)
    except Exception as e:
        print("查询错误:", e)
        return None

    return highest_wind, highest_humidity

# 调用函数并打印结果
highest_wind, highest_humidity = highest_wind_humidity()
print("风速最高的十个城市:", highest_wind)
print("湿度最高的十个城市:", highest_humidity)
