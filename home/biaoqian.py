from .utils import *

def count_weather():
    try:
        # 查询包含阴天的城市数量
        cursor.execute("SELECT COUNT(*) FROM weatherdata WHERE 天气情况 LIKE '%阴%'")
        cloudy_cities = cursor.fetchone()[0]

        # 查询包含晴天的城市数量
        cursor.execute("SELECT COUNT(*) FROM weatherdata WHERE 天气情况 LIKE '%晴%'")
        sunny_cities = cursor.fetchone()[0]

        # 查询包含雨天的城市数量
        cursor.execute("SELECT COUNT(*) FROM weatherdata WHERE 天气情况 LIKE '%雨%'")
        rainy_cities = cursor.fetchone()[0]

        # 查询包含雪天的城市数量
        cursor.execute("SELECT COUNT(*) FROM weatherdata WHERE 天气情况 LIKE '%雪%'")
        snowy_cities = cursor.fetchone()[0]

    except Exception as e:
        print("查询错误:", e)
        return None

    return sunny_cities, cloudy_cities, rainy_cities, snowy_cities


# 调用函数并打印结果
sunny, cloudy, rainy, snowy = count_weather()
print("晴天城市数量:", sunny)
print("阴天城市数量:", cloudy)
print("雨天城市数量:", rainy)
print("雪天城市数量:", snowy)
