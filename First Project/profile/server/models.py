from . import db


class User(db.Model):
    """User model for storing necessary credentials"""
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    number = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)

