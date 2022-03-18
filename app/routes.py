from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/events')
def events():
    return render_template('index.html', title='Events')

@app.route('/jams')
def jams():
    return render_template('index.html', title='Jams')

@app.route('/support')
def support():
    return render_template('index.html', title='Support')

@app.route('/mission')
def mission():
    return render_template('index.html', title='Mission')
