# coding=utf-8
from flask import Flask,session
# 导入配置文件
from settings import Config
# 作用制定session信息存放的位置,对session信息签名和指定过期时间
from flask_session import Session

# 创建进程实例
# 传入__name__参数的作用是确定程序所在的位置
# flask 会默认创建静态路由
# 可以传入字符串。不能传入数值，如果传入python内置的模块名，默认访问的静态文件找不到
app = Flask(__name__)
# 配置对象config，类似于django中的配置文件
app.config.from_object(Config)
# app.config['DEBUG'] = True

# Session(app)

# 设置session
@app.route('/setsession')
def setsession():
    #  CJCKsWgWl/6kU4mmhLoVig4Q2s0BLFXXtqsczQ17LXc/6QXgMiXEyjr+PnLs4M1T0zQ=
    session['name'] = 'newworktest'
    return 'set session success'

# 获取session
@app.route('/getse‘ssion')
def getsession():
    response = session.get('name')
    return response

if __name__ == '__main__':
    app.run()