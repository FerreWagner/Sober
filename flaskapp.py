from flask import Flask,request,url_for,render_template,flash,abort
from models import User
import sys

app = Flask(__name__)


@app.route('/')
def hello_world():
    content = "Glory"
    return render_template("index.html", str_g = content)

@app.route('/user')
def user_index():
    users = User(1, 'For Flower')
    return render_template("user_index.html", user = users)

@app.route('/query_user/<user_id>')
def query_user(user_id):
    user = None
    if int(user_id) == 1:
        user = User(1, 'J-user')
    return render_template("user_id.html", user = user)

@app.route('/users')
def user_list():
    users = []
    for i in range(1, 11):
        user = User(1, 'J-user' + str(i))
        users.append(user)
    return render_template("user_list.html", users = users)

@app.route('/one')
def one_base():
    return render_template("one_base.html")

@app.route('/two')
def two_base():
    return render_template("two_base.html")


#flask的消息闪现机制
app.secret_key = '123'
@app.route('/fla')
def fla():
    flash("flash dead")
    return render_template("fla.html")


@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = request.form
    username = form.get('username')
    password = form.get('password')

    if not username:
        flash("pls input username")
        return render_template("fla.html")
    if not password:
        flash("pls input password")
        return render_template("fla.html")
    if username == 'flower' and password == '123369':
        flash("login success")
        return render_template("fla.html")
    else:
        flash("user or pass error")
        return render_template("fla.html")

#捕获http错误
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")


@app.route('/users/<id>')
def users(id):
    if int(id) == 1:
        return render_template("user.html")

    else:
        abort(404)  #不等于1则抛出404异常


if __name__ == '__main__':
    app.run()
