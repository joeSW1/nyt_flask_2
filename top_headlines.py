from logging import captureWarnings
from flask import Flask, render_template
import json, urllib.request
import requests


api_key = "AyV51ehAf31OGNMb6O3su3s2su9ISYVI"

app = Flask(__name__)
'''
root = "https://api.nytimes.com/svc/topstories/v2/arts.json?api-key="
res = requests.get(root, api_key)
'''


@app.route('/')
def index():
    return render_template('template1.html', name="joe", topic="guns", opinion="guns are bad")


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
