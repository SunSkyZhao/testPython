# 导入了flask类
from flask import Flask
# 创建一个该类的实例
app = Flask(__name__)

# route装饰器确定触发的url
@app.route('/')
def index():
    return "index page!"
@app.route('/test')
def test():
    return 'Hello World'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

# 确保该服务器只在python解释器执行的时候才会运行
if __name__ == '__main__':
    # run函数运行
    app.run()