# coding=utf-8
from flask_script import Manager
from flask import Flask


# flask_script 扩展命令行，作用是可以在终端以命令行的形式启动项目
# 可以自定义ip和port，在生产情况下，手动指定比较方便调试运行代码

app = Flask(__name__)


#　实例化管理器对象
manager = Manager(app)


@app.route('/')
def demo():
    return 'flask_script扩展命令行'

if __name__ == '__main__':
    # app.run 可以指定host和port
    # app.run()
    manager.run()