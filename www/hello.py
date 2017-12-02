from flask import Flask
from flask import make_response
from flask import abort
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/test/<name>')
def test(name):
    return '<h1>Hello {}!</h1>'.format(name)


@app.route('/test1')
def test1():
    return 'Bad Request',400


@app.route('/cookie')
def cookies():
    response = make_response('<h1>this document is carried by cookie</h1>')
    response.set_cookie('answer', 'this document is carried by cookie')
    return response


@app.route('/test_abort')
def test_abort():
    abort(404)


if __name__ == '__main__':
    app.run(debug=True)