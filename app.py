from flask import Flask, render_template, request, redirect, session,jsonify
from werkzeug.security import generate_password_hash

from userUtils.query import query

from home.biaoqian import count_weather
from home.line import highest_lowest_temperature
from home.bar import highest_wind_humidity, highest_wind_weather

from search.line import line, line2
from search.table import table

from lishi.search import search_weather
from map.utils import city_tem
import json

app = Flask(__name__)

# 设置密钥
app.secret_key = 'your_secret_key'


@app.route('/')
def every():
    return render_template('login.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        request.form = dict(request.form)

        email = request.form.get('email')
        password = request.form.get('password')

        user_info = query('SELECT username, email, password FROM users WHERE email = %s', [email], 'select_one')

        user = query('SELECT * FROM users WHERE email = %s AND password = %s', [email, password], 'select_one')

        if user:
            session['username'] = user_info['username']  # 存储用户名
            session['email'] = user_info['email']  # 存储邮箱信息
            return redirect('/home', 301)

        else:
            error_message = '账号或密码错误'
            return render_template('login.html', error_message=error_message)

    else:
        return render_template('login.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        request.form = dict(request.form)
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        password_checked = request.form.get('passwordChecked')

        if password != password_checked:
            error_message = '两次密码不符'
            return render_template('register.html', error_message=error_message)

        email_exists = query('SELECT * FROM users WHERE email = %s', [email], 'select_one')
        if email_exists:
            error_message = '该邮箱已被注册'
            return render_template('register.html', error_message=error_message)

        user_exists = query('SELECT * FROM users WHERE username = %s', [username], 'select_one')
        if user_exists:
            error_message = '用户名已被注册'
            return render_template('register.html', error_message=error_message)

        query('INSERT INTO users (username, email, password) VALUES (%s, %s, %s)', [username, email, password])

        session['email'] = email
        return redirect('/login', 301)

    else:
        return render_template('register.html')


@app.route("/home")
def home():
    # 获取用户信息
    email = session.get('email')
    # 四个标签
    sunny, cloudy, rainy, snowy = count_weather()
    # 折线图
    highest_temperatures, lowest_temperatures = highest_lowest_temperature()

    # 饼图和环形图
    highest_wind, highest_humidity = highest_wind_humidity()

    return render_template('home.html',
                           email=email,
                           # 标签
                           sunny=sunny,
                           cloudy=cloudy,
                           rainy=rainy,
                           snowy=snowy,

                           # 折线图
                           highest_temperatures=highest_temperatures,
                           lowest_temperatures=lowest_temperatures,

                           # 饼图和环形图
                           highest_wind=highest_wind,
                           highest_humidity=highest_humidity
                           )

# 天气地图路由
@app.route('/map')
def map():
    # 获取用户信息
    email = session.get('email')
    data = request.args.get('data', default='温度')  # 如果没有指定县市，默认为'池 州 市'
    temperature = city_tem(data)
    temperature = json.dumps(temperature)  # 将温度数据转换为 JSON 格式
    return render_template('map.html',
                           email=email,
                           temperatureData=temperature
                           )




@app.route('/search', methods=['POST', 'GET'])
def search():
    email = session.get('email')
    try:
        if request.method == 'POST':
            # 接收参数
            city = request.form.get('city')

            # 调用 line 函数获取四个不同的天气指标数据
            line_result = line(city)

            # 调用 table 函数获取天气数据表格
            table_result = table(city)

            # 将四个指标数据分别赋值给不同的变量
            highest, lowest, visibility, humidity = line_result

            # 将结果组织成字典
            search_result = {
                'highest': highest,
                'lowest': lowest,
                'visibility': visibility,
                'humidity': humidity,
                'table_result': table_result  # 将新查询的结果添加到字典中
            }
            print("查询结果:", search_result)
            return jsonify(search_result)
        return render_template('search.html', email=email)
    except Exception as e:
        error_message = "存在错误: {}".format(str(e))
        return jsonify({"error": error_message}), 500


@app.route('/lishi', methods=['POST', 'GET'])
def lishi():
    email = session.get('email')
    try:
        if request.method == 'POST':
            city = request.form.get('city')
            date = request.form.get('date')  # 接收日期参数
            search_result = search_weather(city, date)
            print("查询结果:", search_result)
            return jsonify(search_result)
        return render_template('lishi.html',email=email)
    except Exception as e:
        error_message = "存在错误: {}".format(str(e))
        return jsonify({"error": error_message}), 500

@app.route('/lishi2', methods=['POST', 'GET'])
def lishi2():
    email = session.get('email')
    highest_wind, highest_humidity = highest_wind_weather()

    try:
        if request.method == 'POST':
            # 接收参数
            city = request.form.get('city')
            data = request.form.get('data')

            # 调用 line 函数获取四个不同的天气指标数据
            # line_result = line2(city)

            line_result = line2(city, data)
            # 调用 table 函数获取天气数据表格
            table_result = table(city)

            # 将四个指标数据分别赋值给不同的变量
            highest, lowest = line_result

            # 饼图和环形图


            # 将结果组织成字典
            search_result = {
                'highest': highest,
                'lowest': lowest,

                'table_result': table_result  # 将新查询的结果添加到字典中
            }

            # 饼图和环形图
            print("查询结果:", search_result)
            return jsonify(search_result)
        return render_template('lishi2.html',
                               email=email,
                                highest_wind=highest_wind,
                                highest_humidity=highest_humidity
                               )
    except Exception as e:
        error_message = "存在错误: {}".format(str(e))
        return jsonify({"error": error_message}), 500
# 用户信息获取路由
@app.route('/get_user_info')
def get_user_info():
    username = session.get('username')
    if username:
        user_info = query('SELECT username, email, password, cities FROM users WHERE username = %s', [username],
                          'select_one')
        if user_info:
            # 确保 cities 为列表格式
            user_info['cities'] = json.loads(user_info['cities']) if user_info['cities'] else []
            return jsonify({
                'username': user_info['username'],
                'email': user_info['email'],
                'password': '********',  # 隐藏实际密码
                'cities': user_info['cities']
            })
    return jsonify({}), 404


# 更新用户名路由
@app.route('/update_username', methods=['POST'])
def update_username():
    new_username = request.json.get('newUsername')
    if new_username:
        username = session.get('username')
        if username:
            query('UPDATE users SET username = %s WHERE username = %s', [new_username, username])
            session['username'] = new_username
            return jsonify({'message': '用户名更新成功'})
    return jsonify({'message': '用户名更新失败'}), 400


# 更新邮箱路由
@app.route('/update_email', methods=['POST'])
def update_email():
    new_email = request.json.get('newEmail')
    if new_email:
        username = session.get('username')
        if username:
            query('UPDATE users SET email = %s WHERE username = %s', [new_email, username])
            return jsonify({'message': '邮箱更新成功'})
    return jsonify({'message': '邮箱更新失败'}), 400


# 更新密码路由
@app.route('/update_password', methods=['POST'])
def update_password():
    new_password = request.json.get('newPassword')
    if new_password:
        username = session.get('username')
        if username:
            hashed_password = generate_password_hash(new_password)
            query('UPDATE users SET password = %s WHERE username = %s', [hashed_password, username])
            return jsonify({'message': '密码更新成功'})
    return jsonify({'message': '密码更新失败'}), 400


# 用户管理路由
@app.route('/user')
def user():
    username = session.get('username')
    return render_template('user.html',username=username)

# 假设这是你的有效城市列表，实际应用中这个列表可能来自数据库或其他数据源
VALID_CITIES = ["北京", "海淀", "朝阳", "顺义", "怀柔", "通州", "昌平", "延庆", "丰台",
                "石景山", "大兴", "房山", "密云", "门头沟", "平谷", "上海", "闵行",
                "宝山", "嘉定", "南汇", "金山", "青浦", "松江", "奉贤", "崇明",
                "徐家汇", "浦东", "天津", "武清", "宝坻", "东丽", "西青", "北辰", "宁河",
                "汉沽", "静海", "津南", "塘沽", "大港", "蓟县", "重庆", "永川", "合川",
                "南川", "江津", "万盛", "渝北", "北碚", "巴南", "长寿", "黔江", "万州",
                "涪陵", "开县", "城口", "云阳", "巫溪", "奉节", "巫山", "潼南", "垫江",
                "梁平", "忠县", "石柱", "大足", "荣昌", "铜梁", "璧山", "丰都", "武隆",
                "彭水", "綦江", "酉阳", "秀山", "哈尔滨", "齐齐哈尔", "牡丹江", "佳木斯",
                "绥化", "黑河", "大兴安岭", "伊春", "大庆", "七台河", "鸡西", "鹤岗",
                "双鸭山", "长春", "吉林", "延边", "四平", "通化", "白城", "辽源", "松原",
                "白山", "沈阳", "大连", "鞍山", "抚顺", "本溪", "丹东", "锦州", "营口",
                "阜新", "辽阳", "铁岭", "盘锦", "葫芦岛", "呼和浩特", "包头", "乌海",
                "乌兰察布", "通辽", "赤峰", "鄂尔多斯", "巴彦淖尔", "锡林郭勒", "呼伦贝尔",
                "兴安盟", "阿拉善盟", "石家庄", "保定", "张家口", "承德", "唐山", "廊坊",
                "沧州", "衡水", "邢台", "邯郸", "秦皇岛", "太原", "大同", "阳泉", "晋中",
                "长治", "晋城", "临汾", "运城", "朔州", "忻州", "吕梁", "西安", "咸阳",
                "延安", "榆林", "渭南", "商洛", "安康", "汉中", "宝鸡", "铜川", "杨凌",
                "济南", "青岛", "淄博", "德州", "烟台", "潍坊", "济宁", "泰安", "临沂",
                "菏泽", "滨州", "东营", "威海", "枣庄", "日照", "莱芜", "聊城", "乌鲁木齐",
                "克拉玛依", "石河子", "昌吉", "吐鲁番", "巴州", "阿拉尔", "阿克苏", "喀什",
                "伊犁", "塔城", "哈密", "和田", "阿勒泰", "克州", "博州", "拉萨", "日喀则",
                "山南", "林芝", "昌都", "那曲", "阿里", "西宁", "海东", "黄南", "海南",
                "果洛", "玉树", "海西", "海北", "格尔木", "兰州", "定西", "平凉", "庆阳",
                "武威", "金昌", "张掖", "酒泉", "天水", "陇南", "临夏", "甘南", "白银",
                "嘉峪关", "银川", "石嘴山", "吴忠", "固原", "中卫", "郑州", "安阳", "新乡",
                "许昌", "平顶山", "信阳", "南阳", "开封", "洛阳", "商丘", "焦作", "鹤壁",
                "濮阳", "周口", "漯河", "驻马店", "三门峡", "济源", "南京", "无锡", "镇江",
                "苏州", "南通", "扬州", "盐城", "徐州", "淮安", "连云港", "常州", "泰州",
                "宿迁", "武汉", "襄阳", "鄂州", "孝感", "黄冈", "黄石", "咸宁", "荆州",
                "宜昌", "恩施", "十堰", "神农架", "随州", "荆门", "天门", "仙桃", "潜江",
                "杭州", "湖州", "嘉兴", "宁波", "绍兴", "台州", "温州", "丽水", "金华",
                "衢州", "舟山", "合肥", "蚌埠", "芜湖", "淮南", "马鞍山", "安庆", "宿州",
                "阜阳", "亳州", "黄山", "滁州", "淮北", "铜陵", "宣城", "六安", "巢湖",
                "池州", "福州", "厦门", "宁德", "莆田", "泉州", "漳州", "龙岩", "三明",
                "南平", "南昌", "九江", "上饶", "抚州", "宜春", "吉安", "赣州", "景德镇",
                "萍乡", "新余", "鹰潭", "长沙", "湘潭", "株洲", "衡阳", "郴州", "常德",
                "益阳", "娄底", "邵阳", "岳阳", "张家界", "怀化", "永州", "湘西", "贵阳",
                "遵义", "安顺", "黔南", "黔东南", "铜仁", "毕节", "六盘水", "黔西南",
                "成都", "攀枝花", "自贡", "绵阳", "南充", "达州", "遂宁", "广安", "巴中",
                "泸州", "宜宾", "内江", "资阳", "乐山", "眉山", "凉山", "雅安", "甘孜",
                "阿坝", "德阳", "广元", "广州", "韶关", "惠州", "梅州", "汕头", "深圳",
                "珠海", "佛山", "肇庆", "湛江", "江门", "河源", "清远", "云浮", "潮州",
                "东莞", "中山", "阳江", "揭阳", "茂名", "汕尾", "昆明", "大理", "红河",
                "曲靖", "保山", "文山", "玉溪", "楚雄", "普洱", "昭通", "临沧", "怒江",
                "迪庆", "丽江", "德宏", "西双版纳", "南宁", "崇左", "柳州", "来宾", "桂林",
                "梧州", "贺州", "贵港", "玉林", "百色", "钦州", "河池", "北海", "防城港",
                "香港", "澳门", "台北", "高雄", "台中", "海口", "三亚", "三沙"
]


# 添加关注的城市
@app.route('/add_city', methods=['POST'])
def add_city():
    username = session.get('username')
    if not username:
        return jsonify({'message': '用户未登录'}), 401

    new_city = request.json.get('newCity')
    if not new_city:
        return jsonify({'message': '城市名称不能为空'}), 400

    # 检查城市名称是否有效
    if new_city not in VALID_CITIES:
        return jsonify({'message': '无效的城市名称'}), 400

    # 从数据库获取当前用户的 cities 列表
    user_info = query('SELECT cities FROM users WHERE username = %s', [username], 'select_one')
    if user_info and 'cities' in user_info:
        cities = json.loads(user_info['cities']) if user_info['cities'] else []
    else:
        cities = []

    # 添加新城市（去重）
    if new_city not in cities:
        cities.append(new_city)

    # 更新数据库
    query('UPDATE users SET cities = %s WHERE username = %s', [json.dumps(cities), username])
    return jsonify({'message': '城市添加成功', 'cities': cities})


@app.route('/remove_city', methods=['POST'])
def remove_city():
    username = session.get('username')
    if not username:
        return jsonify({'message': '用户未登录'}), 401

    cities_to_remove = request.json.get('citiesToRemove')
    if not cities_to_remove:
        return jsonify({'message': '没有提供城市名称'}), 400

    # 从数据库获取当前用户的 cities 列表
    user_info = query('SELECT cities FROM users WHERE username = %s', [username], 'select_one')
    if user_info and 'cities' in user_info:
        cities = json.loads(user_info['cities']) if user_info['cities'] else []
    else:
        cities = []

    # 移除选中的城市
    cities = [city for city in cities if city not in cities_to_remove]

    # 更新数据库
    query('UPDATE users SET cities = %s WHERE username = %s', [json.dumps(cities), username])
    return jsonify({'message': '删除成功', 'cities': cities})

if __name__ == '__main__':
    app.run(debug=True)
