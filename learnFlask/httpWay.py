# 导入了flask类
from flask import Flask
# 创建一个该类的实例
app = Flask(__name__)

# route装饰器确定触发的url
@app.route('/login',methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()

# 模版渲染
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html',name=name)

# 确保该服务器只在python解释器执行的时候才会运行
if __name__ == '__main__':
    # run函数运行
    app.run()