import re

import pymysql
from pymysql import *

# 设置数据库连接信息
conn = connect(host='localhost', user='root', password='123456', database='tianqi', port=3306)
cursor = conn.cursor()


def query(sql, params, query_type='no_select'):
    params = tuple(params)
    cursor.execute(sql, params)

    if query_type == 'select_one':
        # 对于 select_one 查询，返回单个结果的字典
        data = cursor.fetchone()  # 使用 fetchone 获取单个结果
        if data:
            # 将元组转换为字典，假设列名可以通过 cursor.description 获取
            keys = [col[0] for col in cursor.description]
            return dict(zip(keys, data))
        else:
            return None  # 如果没有结果，返回 None
    else:
        # 对于其他类型的数据库操作，提交事务并返回成功消息
        conn.commit()
        return '数据库语句执行成功'



#
# def query(sql, params, type='no_select'):
#     params = tuple(params)
#     cursor.execute(sql, params)
#     if type != 'no_select':
#         data_list = cursor.fetchall()
#         conn.commit()
#         return data_list
#     else:
#         conn.commit()
#         return '数据库语句执行成功'


# 定义一个函数，用于将数据框中的数据保存到 mysql 数据表中
def save_to_mysql(datas, city):  # 添加城市参数
    for i in range(len(datas)):
        date = datas.iloc[i, 0]
        max_temp = float(re.findall(r'\d+', datas.iloc[i, 1])[0])
        min_temp = float(re.findall(r'\d+', datas.iloc[i, 2])[0])
        weh = datas.iloc[i, 3]
        wind = datas.iloc[i, 4]
        # 在 SQL 语句中包含城市信息
        sql = "INSERT INTO lishiweathers (城市, 日期, 最高温度, 最低温度, 天气, 风向) VALUES ('{}', '{}', {}, {}, '{}', '{}')".format(
            city, date, max_temp, min_temp, weh, wind)
        cursor.execute(sql)
    conn.commit()
    print("成功将数据保存到 lishiweathers 表中")


# 将当前天气数据保存到数据库
def save_current_weather_to_database(city_name, current_weather_data):
    try:
        # connection = pymysql.connect(**db_config)
        # cursor = connection.cursor()

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

        conn.commit()
        print(f"当前天气数据保存成功: {city_name}")

    except pymysql.Error as err:
        print(f"数据库错误: {err}")

    # finally:
    #     if conn:
    #         cursor.close()
    #         conn.close()

def connect_to_database():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='123456',
        db='tianqi',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

def search_table(table_name):
    connection = connect_to_database()
    with connection.cursor() as cursor:
        sql = f"SELECT chengshi, yuceshijian, qiwen,shidu, qiya,fengsu,fengxiang,jiangyu FROM {table_name} "
        # sql = f"SELECT * FROM {table_name} "
        cursor.execute(sql)

        # cursor.execute(sql)
        result = cursor.fetchall()
        return result


def search_warning(table_name,city,data1):
    connection = connect_to_database()
    with connection.cursor() as cursor:
        # sql = f"SELECT * FROM {table_name} WHERE 城市 = %s AND 类型名称 = %s"
        sql = f"SELECT * FROM {table_name} WHERE `城市` LIKE %s AND `类型名称` LIKE %s"
        city = '%' + city + '%'
        data1 = '%' + data1 + '%'  # 修改日期的模糊匹配

        # sql = f"SELECT * FROM {table_name} WHERE 城市 LIKE %s AND 类型名称 LIKE %s"
        cursor.execute(sql, (city, data1))

        # cursor.execute(sql)
        result = cursor.fetchall()
        return result

def search_recommend(table_name,city,data1):
    connection = connect_to_database()
    with connection.cursor() as cursor:
        # sql = f"SELECT * FROM {table_name} WHERE 城市 = %s AND 类型名称 = %s"
        sql = f"SELECT * FROM {table_name} WHERE `城市` LIKE %s AND `生活指数类型` LIKE %s"
        city = '%' + city + '%'
        data1 = '%' + data1 + '%'  # 修改日期的模糊匹配

        # sql = f"SELECT * FROM {table_name} WHERE 城市 LIKE %s AND 类型名称 LIKE %s"
        cursor.execute(sql, (city, data1))

        # cursor.execute(sql)
        result = cursor.fetchall()
        return result