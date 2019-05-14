from flask import Flask,request,url_for,render_template
from models import User

app = Flask(__name__)


@app.route('/')
def hello_world():
    content = "Glory"
    return render_template("index.html", str_g = content)

@app.route('/user')
def user_index():
    users = User(1, 'For Flower')
    return render_template("user_index.html", user = users)

if __name__ == '__main__':
    app.run()
