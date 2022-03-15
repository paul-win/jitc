from app import db
from datetime import datetime

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    event_date = db.Column(db.DateTime, nullable=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'))
    artist = db.relationship('Artist', foreign_keys=[artist.id])
    jams = db.relationship('Jam', lazy='dynamic')
    updated = db.Column(db.DateTime, index=True, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return '<Event: {}-{}>'.format(self.title, self.event_date)


class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    
    def __repr__(self):
        return '<Artist: {}>'.format(self.name)


class Jam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
    event = db.relationship('Event', foreign_keys=[event_id])
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'))
    artist = db.relationship('Artist', foreign_keys=[artist_id])
    track_num = db.Column(db.SmallInteger)
    title = db.Column(db.String(120))

    def __repr__(self):
        return '<Jam: {}-{}.{}>'.format(self.artist.name, self.track_num, self.title)
