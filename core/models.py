import datetime
from uuid import uuid4

from sqlalchemy.dialects.postgresql import UUID

from core.config import db


class Users(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    user_address = db.Column(db.String(200))
    create_user_date = db.Column(db.DateTime, default=datetime.datetime.utcnow().isoformat())

    def __repr__(self):
        return '<User {}'.format(self.username)
