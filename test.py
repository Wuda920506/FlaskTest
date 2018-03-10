from flask import Flask

# 创建进程实例
app = Flask(__name__)

# 定义视图
@app.route('/')
def index():
    return "hello world!"

# 启动服务器
if __name__ == '__main__':
    app.run()