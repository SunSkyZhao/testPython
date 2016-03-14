from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/login',methods=['POST','GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'maobi'

    return render_template('login.html',error = error)