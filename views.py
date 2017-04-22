import pafy
from flask import render_template

from app import app


@app.route('/')
def hello_world():
    return 'Hello, World! YALAAA'


@app.route('/lala')
def index():
    return '<h1>You are on the index!</h1>'


@app.route('/test')
def info():
    playlist = pafy.get_playlist("PLpaD0ybYH0S1yYJAGHhHgJE46oEfGfl2C")
    videos = playlist['items']

    listing = []

    for video in videos:
        p = video['pafy']
        listing.append(p.title)

    return render_template('test.html', info=listing)
