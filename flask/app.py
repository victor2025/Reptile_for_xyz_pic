from flask import Flask,render_template
import datetime

app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return 'hello'

@app.route('/index')
def test_1():
    return 'hello_1'

@app.route('/user/<name>')
def welcom_1(name):
    return 'Hello,'+name

@app.route('/user/<int:id>')
def welcom_2(id):
    return 'Hello,%d 号的会员'%id

# @app.route('/')
# def index_2():
#     return render_template('index.html')

@app.route('/')
def index_3():
    time = datetime.date.today()
    name = ['李','恒','威']
    return render_template('index.html',var = time,list = name)


if __name__ == '__main__':
    app.run()
