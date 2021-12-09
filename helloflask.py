from logging import captureWarnings
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/about')
def about():
    html = '''
        <h1>About this Site </h1>
        <p>This is my first ever Flask website! </p>
        <a href='/'>Go Back home </a>
    '''
    return html

ctr = 0
@app.route('/counter')
def counter():
    global ctr 
    ctr += 1
    return '<h3>' + str(ctr) + '</h3>'

def my_func():
    print('hello')

def my_decorator(dec_func):
    print('calling the decorated function')
    dec_func()
    print('called the decorated function')

my_decorator(my_func)

if __name__=='__main__':
    print('starting Flask app', app.name)
    app.run(debug=True)
