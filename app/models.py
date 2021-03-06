from app import db
from flask import url_for
from datetime import datetime, timedelta
import os
from markupsafe import escape, Markup

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    event_door = db.Column(db.DateTime, nullable=False)
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
    thumbnail = db.Column(db.String(64))
    active_item = False
    updated = db.Column(db.DateTime, index=True, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return '<Event: {}-{}>'.format(self.title, self.event_door)
    def verbose_title(self, include_time=True):
        if include_time:
            return 'Jam in the Can presents: {} @ {}, {}'.format(self.title, self.venue.name, self.event_door.strftime('%A %B %-d, %Y %-I:%M%p'))
        else:
            return 'Jam in the Can presents: {} @ {}, {}'.format(self.title, self.venue.name, self.event_door.strftime('%B %-d, %Y'))
    def page_title(self):
        return '{} - {}'.format(self.title, self.event_door.strftime('%B %-d, %Y'))
    def get_media_dir_path(self):
        if self.media_dir:
            return os.getcwd() + '/app/static/' + self.media_dir
        else:
            return ''
    def media_files(self):
        dir_path = self.get_media_dir_path()
        if dir_path:
            return os.listdir(dir_path)
        else:
            return []
    def get_file_path(self, filename):
        res = ''
        if filename:
            dir_path = self.get_media_dir_path()
            file_path = dir_path + filename
            if dir_path and os.path.exists(file_path):
                res = self.media_dir + filename
        return res
    def cover_card_path(self):
        file_path = self.get_file_path('cover_card.jpg')
        if file_path:
            return file_path
        else:
            return ''
    def cover_photo_path(self):
        file_path = self.get_file_path('cover.jpg')
        if file_path:
            return file_path
        # elif self.thumbnail:
        #     return self.get_file_path(self.thumbnail)
        else:
            file_path = self.venue.cover_photo_path()
            if file_path:
                return file_path
            else:
                return ''
    def upcoming(self):
        return self.event_door.date() >= (datetime.utcnow() - timedelta(hours=5)).date()
    def price_two_places(self):
        if self.price:
            return round(self.price, 2)
        else:
            return None
    def about_html(self):
        if self.about:
            return Markup(self.about.replace('\n', '</p><p>'))
        else:
            return ''
    def jam_album_title(self):
        return 'Jam in the Can Live {}'.format(self.event_door.strftime('%-m-%-d-%Y'))
    def has_jams(self):
        return len(self.jams) > 0
    def jams_to_json(self):
        return [jam.to_json() for jam in self.jams]

class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    
    def __repr__(self):
        return '<Artist: {}>'.format(self.name)
    def safe_name(self):
        return escape(self.name)

class Venue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    street_address = db.Column(db.String(120))
    city = db.Column(db.String(64))
    state = db.Column(db.String(8))
    zip = db.Column(db.String(16))
    media_dir = db.Column(db.String(128))
    info = db.Column(db.String(120))

    def __repr__(self):
        return '<Venue: {}>'.format(self.name)
    def get_media_dir_path(self):
        if self.media_dir:
            return os.getcwd() + '/app/static/' + self.media_dir
        else:
            return ''
    def media_files(self):
        dir_path = self.get_media_dir_path()
        if dir_path:
            return os.listdir(dir_path)
        else:
            return []
    def get_file_path(self, filename):
        dir_path = self.get_media_dir_path()
        file_path = dir_path + filename
        if dir_path and os.path.exists(file_path):
            return self.media_dir + filename
        else:
            return ''
    def cover_photo_path(self):
        file_path = self.get_file_path('cover.jpg')
        if file_path:
            return file_path
        else:
            return ''

class Jam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
    event = db.relationship('Event', back_populates="jams")
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'))
    artist = db.relationship('Artist', foreign_keys=[artist_id])
    track_num = db.Column(db.SmallInteger, nullable=False)
    title = db.Column(db.String(120))
    length = db.Column(db.Time)
    file = db.Column(db.String(128))

    def __repr__(self):
        return '<Jam: {}-{}.{}>'.format(self.artist.name, self.track_num, self.title)
    def to_json(self):
        return {
            "name": self.title,
            "artist": self.artist.name,
            "album": self.event.jam_album_title(),
            "url": url_for('static', filename=self.event.media_dir + self.file),
            # "cover_art_url": "../album-art/we-are-to-answer.jpg"
        }