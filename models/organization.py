from datetime import datetime
from models.database import db


class Organization(db.Model):
    __tablename__ = 'organizations'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    domain = db.Column(db.String(150), nullable=False)
    type = db.Column(db.String(20), nullable=False)  # 'provider' or 'client'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    users = db.relationship('User', backref='organization', lazy=True)

    def __repr__(self):
        return f'<Organization {self.name}>'