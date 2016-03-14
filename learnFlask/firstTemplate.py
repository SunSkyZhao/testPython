# # 导入了render_template类
# from flask import render_template
# # 创建一个该类的实例
# app = render_template(__name__)
#
# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name=name)
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


# 确保该服务器只在python解释器执行的时候才会运行
if __name__ == '__main__':
    # run函数运行
    app.run()