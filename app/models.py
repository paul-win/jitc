from app import db
from datetime import datetime

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    event_date = db.Column(db.DateTime, nullable=True)
    updated = db.Column(db.DateTime, index=True, default=datetime.utcnow, nullable=False)

    def __repr__(self):
            return '<Event: {}-{}>'.format(self.title, self.event_date)
