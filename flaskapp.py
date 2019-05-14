from flask import Flask,request,url_for,render_template
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





if __name__ == '__main__':
    app.run()
