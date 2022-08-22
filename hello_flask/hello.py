from flask import Flask
from functools import wraps
app = Flask(__name__)

def make_bold(function):
    def bold_wrapper(*args, **kwargs):
        return f'<b>{function(*args, **kwargs)}</b>'
    return bold_wrapper

def add_emphasis(function):
    def em_wrapper(*args, **kwargs):
        return f'<em>{function(*args, **kwargs)}</em>'
    return em_wrapper

def center(function):
    @wraps(function)
    def cent_wrapper(*args, **kwargs):
        return f'<div style="text-align: center">{function(*args, **kwargs)}</div>'
    return cent_wrapper

def underline(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        return f'<u>{function(*args, **kwargs)}</u>'
    return wrapper

@app.route('/')
@center
@add_emphasis
def hello():
    return '<h1>Hello World!</h1>' \
            '<p>This is a paragraph.</p>' \
            '<img src="https://media4.giphy.com/media/11s7Ke7jcNxCHS/200.webp" width=200>'

@app.route('/bye')
@center
@make_bold
@add_emphasis
def bye():
    return 'Bye!'

@app.route('/username/<name>/<int:number>')
@center
def greet(name, number):
    return f'Hello {name}! You are {number} years old.'

if __name__ == '__main__':
    app.run(debug=True)