from app import db
from datetime import datetime, timezone

class PushEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    repository = db.Column(db.String(120))
    message = db.Column(db.Text)
    url = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    @staticmethod
    def create(repository, message, url):
        event = PushEvent(repository=repository, message=message, url=url)
        db.session.add(event)
        db.session.commit()
        return event

    @staticmethod
    def get_all_desc():
        return PushEvent.query.order_by(PushEvent.timestamp.desc()).all()