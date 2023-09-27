from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello, flask'

@app.route('/sub1')
def sub1():
    return 'SUB1 Page'


if __name__ == '__main__':
    app.run(host='0.0.0.0' , port = 80 )