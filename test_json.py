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
    # return json.dumps(temp)
    return jsonify(temp)

if __name__ == '__main__':
    app.run()