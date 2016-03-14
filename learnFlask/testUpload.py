import os
from flask import Flask,request,url_for,redirect, render_template
from werkzeug import secure_filename

UPLOAD_FOLDER = 'path/to/the/uploads'
ALLOWED_EXTENSIONS = set(['txt','png','jpg','jpeg'])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

@app.route('/',methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            return redirect(url_for('upload_file',filename = filename))
    return

    print("<!doctype html><title>Upload new File</title><h1>Upload new File</h1><form action="" method=post enctype=multipart/form-data><p><input type=file name=file><input type=submit value=Upload></form>")


# 确保该服务器只在python解释器执行的时候才会运行
if __name__ == '__main__':
    # run函数运行
    app.run()