from app import db
from datetime import datetime

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    event_door = db.Column(db.DateTime, nullable=True)
    event_start = db.Column(db.DateTime, nullable=True)
    event_end = db.Column(db.DateTime, nullable=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'))
    artist = db.relationship('Artist', foreign_keys=[artist_id])
    jams = db.relationship('Jam', back_populates="event")
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'))
    venue = db.relationship('Venue', foreign_keys=[venue_id])
    price = db.Column(db.Numeric(precision=2), default=0, nullable=False)
    ticket_link = db.Column(db.String(512))
    ages = db.Column(db.String(8))
    about = db.Column(db.String(2048))
    media_dir = db.Column(db.String(128))
    updated = db.Column(db.DateTime, index=True, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return '<Event: {}-{}>'.format(self.title, self.event_door)


class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    
    def __repr__(self):
        return '<Artist: {}>'.format(self.name)

class Venue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    street_address = db.Column(db.String(120))
    city = db.Column(db.String(64))
    state = db.Column(db.String(8))
    zip = db.Column(db.SmallInteger)
    info = db.Column(db.String(120))

    def __repr__(self):
        return '<Venue: {}>'.format(self.name)

class Jam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
    event = db.relationship('Event', back_populates="jams")
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'))
    artist = db.relationship('Artist', foreign_keys=[artist_id])
    track_num = db.Column(db.SmallInteger, nullable=False)
    title = db.Column(db.String(120))
    file = db.Column(db.String(128))

    def __repr__(self):
        return '<Jam: {}-{}.{}>'.format(self.artist.name, self.track_num, self.title)
