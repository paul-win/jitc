from flask import redirect, render_template, url_for
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
    return render_template('under_construct.html', title='Events')

@app.route('/events/<year>/<month>/<day>/<artist>/<int:event_id>')
def event(year, month, day, artist, event_id):
    ev = Event.query.get(event_id)
    if not ev:
        return redirect(url_for('.index'))
    else:
        return render_template('event.html', title=ev.title, event=ev, background=ev.cover_photo_path())

@app.route('/jams')
def jams():
    return render_template('under_construct.html', title='Jams')

@app.route('/support')
def support():
    return render_template('support.html', title='Support')

@app.route('/mission')
def mission():
    return render_template('mission.html', title='Mission')
