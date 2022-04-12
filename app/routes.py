from flask import redirect, render_template, url_for, json
from sqlalchemy import func
from datetime import datetime
from app import app
from app.models import Event

@app.route('/')
@app.route('/index')
def index():
    events = Event.query.order_by(Event.updated.desc()).limit(5).all()
    if len(events):
        events[0].active_item = True
    return render_template('index.html', title='A non-profit org dedicated to fostering musical arts in Cincinnati, OH', events=events)

@app.route('/events')
def events():
    return render_template('under_construct.html', title='Upcoming and past events')

@app.route('/events/<int:year>/<int:month>/<int:day>/<artist>')
def event(year, month, day, artist):
    dt = datetime(year, month, day)
    evs = Event.query.filter(func.date(Event.event_door) == dt).all()
    for e in evs:
        if e.artist.name == artist:
            ev = e
    if not ev:
        return redirect(url_for('.index'))
    else:
        jams = json.dumps(ev.jams_to_json())
        return render_template('event.html', title=ev.page_title(), event=ev, background=ev.cover_photo_path(), jams=jams)

@app.route('/jams')
def jams():
    return render_template('under_construct.html', title='Music from local Cincinnati, OH artists recorded by Jam in the Can')

@app.route('/support')
def support():
    return render_template('support.html', title='Donate to foster musical arts in Cincinnati, OH')

@app.route('/mission')
def mission():
    return render_template('mission.html', title='We showcase local Cincinnati artists with the goal of supporting the next generation')

@app.route('/store')
def store():
    return render_template('store.html', title="Shop merchandise to support the Jam in the Can mission")
