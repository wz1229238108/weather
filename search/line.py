from .utils import *

def line(city):
    try:
        # 查询最高温度
        cursor.execute("SELECT 观测时间, 最高温度 FROM weatherdata7 WHERE 城市 = %s", (city,))
        highest = cursor.fetchall()
        highest = [(date.strftime("%m月%d日"), temp) for date, temp in highest]

        # 查询最低温度
        cursor.execute("SELECT 观测时间, 最低温度 FROM weatherdata7 WHERE 城市 = %s", (city,))
        lowest = cursor.fetchall()
        lowest = [(date.strftime("%m月%d日"), temp) for date, temp in lowest]

        # 查询紫外线指数
        cursor.execute("SELECT 观测时间, 能见度 FROM weatherdata7 WHERE 城市 = %s", (city,))
        visibility = cursor.fetchall()
        visibility = [(date.strftime("%m月%d日"), index) for date, index in visibility]

        # 查询湿度
        cursor.execute("SELECT 观测时间, 湿度 FROM weatherdata7 WHERE 城市 = %s", (city,))
        humidity = cursor.fetchall()
        humidity = [(date.strftime("%m月%d日"), hum) for date, hum in humidity]

        # 将结果存储在列表中
        result_list = [highest, lowest, visibility, humidity]

    except Exception as e:
        print("查询错误:", e)
        return None

    return result_list

def line2(city,data):
    try:
        # 查询最高温度
        # cursor.execute("SELECT 日期, 最高温度 FROM lishiweathers WHERE 城市 = %s ", (city,))
        cursor.execute("SELECT 日期, 最高温度 FROM lishiweathers WHERE 城市 = %s AND `日期` LIKE CONCAT('%%', %s, '%%')",
                       (city, data,))
        highest = cursor.fetchall()
        highest = [(date.strftime("%m月%d日"), temp) for date, temp in highest]

        # 查询最低温度
        # cursor.execute("SELECT 日期, 最低温度 FROM lishiweathers WHERE 城市 = %s ", (city,))
        cursor.execute("SELECT 日期, 最低温度 FROM lishiweathers WHERE 城市 = %s AND `日期` LIKE CONCAT('%%', %s, '%%')",
                       (city, data,))
        lowest = cursor.fetchall()
        lowest = [(date.strftime("%m月%d日"), temp) for date, temp in lowest]

        # # 查询紫外线指数
        # cursor.execute("SELECT 观测时间, 能见度 FROM weatherdata7 WHERE 城市 = %s", (city,))
        # visibility = cursor.fetchall()
        # visibility = [(date.strftime("%m月%d日"), index) for date, index in visibility]
        #
        # # 查询湿度
        # cursor.execute("SELECT 观测时间, 湿度 FROM weatherdata7 WHERE 城市 = %s", (city,))
        # humidity = cursor.fetchall()
        # humidity = [(date.strftime("%m月%d日"), hum) for date, hum in humidity]

        # 将结果存储在列表中
        # result_list = [highest, lowest, visibility, humidity]
        result_list = [highest, lowest]
        print("result_list",result_list)
    except Exception as e:
        print("查询错误:", e)
        return None

    return result_list
