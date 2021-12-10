from logging import captureWarnings
from flask import Flask, render_template, request
import json, urllib.request
import requests
from secret import api_key

app = Flask(__name__)
root = "https://api.nytimes.com/svc/topstories/v2/technology.json?api-key="
temp = root + api_key

dictionary = []

with urllib.request.urlopen(temp) as url:
    data = json.loads(url.read().decode())
    #print(json.dumps(data, indent=2))
    #print(data["features"][0]["geometry"])
    #array.append(data['results'][0])
    #array.append(data['results'][1])
    #array.append(data['results'][2])
    for result in data["results"]:
        set = {}
        set['title'] = result['title']
        set['url'] = result['url']
        set['image'] = result['multimedia'][0]['url']
        dictionary.append(set)


@app.route('/')
def index():
    return render_template('template1.html')

@app.route('/name/<path:text>', methods=['GET', 'POST'])
def name(text):
    return render_template('name.html', name=text)
    
@app.route('/headlines/<path:text>', methods=['GET', 'POST'])
def headlines(text):
    if text:
        name = text
    else:
        name = "User"
    return render_template('headlines.html', items=dictionary[:5], name=name)
    #return render_template('template1.html', name="joe", topic="guns", opinion="guns are bad")

@app.route('/links/<path:text>', methods=['GET', 'POST'])
def links(text):
    if text:
        name = text
    else:
        name = "User"
    return render_template('links.html', items=dictionary[:5], name=name)
    #return render_template('template1.html', name="joe", topic="guns", opinion="guns are bad")

@app.route('/images/<path:text>', methods=['GET', 'POST'])
def images(text):
    if text:
        name = text
    else:
        name = "User"
    return render_template('images.html', items=dictionary[:5], name=name)
    #return render_template('template1.html', name="joe", topic="guns", opinion="guns are bad")

@app.route('/about')
def about():
    print("test")
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
