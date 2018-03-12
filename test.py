# coding=utf-8
from flask import Flask,session, make_response, current_app, request
# 导入配置文件
from settings import Config
# 导入转换器基类
from werkzeug.routing import BaseConverter

# 创建进程实例
# 传入__name__参数的作用是确定程序所在的位置
# flask 会默认创建静态路由
# 可以传入字符串。不能传入数值，如果传入python内置的模块名，默认访问的静态文件找不到
app = Flask(__name__)
# 配置对象config，类似于django中的配置文件
app.config.from_object(Config)
# app.config['DEBUG'] = True


# 自定义转换器
class Regex(BaseConverter):

    def __init__(self, map, *args):
        # 重写父类__init__
        super(Regex, self).__init__(map)
        # args就是正则表达式
        self.regex = args[0]

        # 测试数据
        print("---map", map)
        print("---args", args[0])


# 添加转换器到程序实例上
app.url_map.converters['re'] = Regex


# 限制访问,优化访问路径
# @app.route('/<re("[a-z]{3}"):name>')
# def demo4(name):
#     return 'demo4:%s' % name


# 原始的静态文件访问路径
# http://127.0.0.1:5000/static/html/detail.html
# 优化后的访问路径
# http://127.0.0.1:5000/detail.html

# 优化访问路径,访问静态文件
@app.route('/<re(".*"):filename>')
def test4(filename):
    if not filename:
        filename = 'index.html'
    else:
        filename = 'html/' + filename
    # 把具体的文件返回给浏览器,make_response,current_app
    response = make_response(current_app.send_static_file(filename))
    return response


# 状态保持,http协议是无状态的,TCP/IP协议,三次握手四次挥手
# cookie和session的区别:
@app.route('/setcookie')
def test3():
    response = make_response('set cookie success')
    response.set_cookie('user', 'python24', max_age=300)
    return response


# 获取cookie,使用请求对象request
@app.route('/getcookie')
def test2():
    response = request.cookies.get('user')
    return response


# 动态路由参数,语法格式<>,默认的数据的类型为str,兼容数值
# 数值之间不兼容,只能限制数据类型,不能限制数据长度
# @app.route('/<int:num>')
# def test1(num):
#     return 'test1:%s' % num


# 定义视图
@app.route('/')
def index():
    return "hello world!"


# 启动服务器
if __name__ == '__main__':
    app.run(debug=True)    # 仅仅在测试的时候打开debug测试模式
