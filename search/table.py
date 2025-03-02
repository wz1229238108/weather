from .utils import *

def table(city):
    try:
        # 查询观测时间、最高温度、最低温度、白天天气状况、晚间天气状况、降水量、能见度和云量
        cursor.execute("""
            SELECT 观测时间, 最高温度, 最低温度, 白天天气状况, 晚间天气状况, 降水量, 能见度, 云量 
            FROM weatherdata7 
            WHERE 城市 = %s
        """, (city,))
        rows = cursor.fetchall()

        # 将结果存储在列表中
        table_list = [(date.strftime("%m月%d日"), high_temp, low_temp, day_weather, night_weather, precipitation, visibility, cloudiness)
                       for date, high_temp, low_temp, day_weather, night_weather, precipitation, visibility, cloudiness in rows]

    except Exception as e:
        print("查询错误:", e)
        return None

    return table_list
