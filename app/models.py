from app import db
from sys import platform
from time import time


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    major = db.Column(db.String(120), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    first_registration = db.Column(db.DateTime)
    logins = db.relationship('Logins', backref='user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.email


class Logins(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    time = db.Column(db.Float, nullable=False)
    system = db.Column(db.String(120), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
                        nullable=False)

    def __repr__(self):
        return '<User %r>' % self.user