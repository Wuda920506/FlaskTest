# coding=utf-8
from flask import Flask, jsonify
from settings import Config


app = Flask(__name__)
app.config.from_object(Config)

"""
字典
dict = '{"age":16, "name":"json"}'

json本质是字符串，基于键值对的字符串。作用是传输数据

xml格式:
<xml>
    <name>json</name>
    <age>16</age>
</xml>

区别:
1.都是用来数据交互的
2.json更轻量

"""
import json

@app.route('/json')
def demo1():
    temp = {"name": "json", "age": 18}
    return json.dumps(temp)
    # return jsonify(temp)

# 返回状态码, 通过return直接返回，可以返回不符合http协议的状态码
# 意义： 主要实现钱后端的数据交互
# return jsonify(error=666, errmsg='用户名或密码错误')
@app.route('/status')
def demo2():
    return '状态码返回', 666

if __name__ == '__main__':
    app.run()