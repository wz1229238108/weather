from .utils import connect_to_database

def search_weather(city, date):
    connection = connect_to_database()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT `城市`, `日期`, `最高温度`, `最低温度`, `天气`, `风向` FROM lishiweathers WHERE `城市` LIKE %s AND `日期` LIKE %s"
            city = '%' + city + '%'
            date = '%' + date + '%'  # 修改日期的模糊匹配
            cursor.execute(sql, (city, date))
            result = cursor.fetchall()
            return result
    finally:
        connection.close()
