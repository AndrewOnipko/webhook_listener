from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
from app import db

class PushEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    repository = db.Column(db.String(120))
    message = db.Column(db.Text)
    url = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))