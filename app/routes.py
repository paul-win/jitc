from flask import render_template
from app import app
from app.models import Event

@app.route('/')
@app.route('/index')
def index():
    events = Event.query.order_by(Event.updated.desc()).limit(5).all()
    if len(events):
        events[0].active_item = True
    return render_template('index.html', title='Home', events=events)

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
    return render_template('mission.html', title='Mission')
