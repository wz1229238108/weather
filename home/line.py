from .utils import *

def highest_lowest_temperature():
    try:
        # 查询温度最高的十个城市名称和温度
        cursor.execute("SELECT 城市, 温度 FROM weatherdata ORDER BY 温度 DESC LIMIT 10")
        highest_temperatures = cursor.fetchall()

        # 查询温度最低的十个城市名称和温度
        cursor.execute("SELECT 城市, 温度 FROM weatherdata ORDER BY 温度 ASC LIMIT 10")
        lowest_temperatures = cursor.fetchall()

    except Exception as e:
        print("查询错误:", e)
        return None

    return highest_temperatures, lowest_temperatures


# 调用函数并打印结果
highest_temperatures, lowest_temperatures = highest_lowest_temperature()
print("温度最高的十个城市:", highest_temperatures)
print("温度最低的十个城市:", lowest_temperatures)
