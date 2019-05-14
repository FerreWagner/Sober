from flask import Flask,request,url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello j!'

@app.route('/flower', methods=['GET'])
def faceless():
    return 'faceless folwer'

@app.route('/buy/<num>')
def buy(num):
    return num

@app.route('/query')
def query():
    id = request.args.get('id')
    return 'query: ' + id

# 反向路由
@app.route('/query_url')
def query_url():
    return 'query_url: ' + url_for('query')


if __name__ == '__main__':
    app.run()
