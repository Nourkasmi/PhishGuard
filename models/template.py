from datetime import datetime
from models.database import db


class Template(db.Model):
    __tablename__ = 'templates'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    institution = db.Column(db.String(100), nullable=False)  # CNSS, STB, etc.
    language = db.Column(db.String(5), nullable=False)  # 'ar' or 'fr'
    subject = db.Column(db.String(255), nullable=False)
    html_content = db.Column(db.Text, nullable=False)
    landing_page = db.Column(db.String(150), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Template {self.name}>'