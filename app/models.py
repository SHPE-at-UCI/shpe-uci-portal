from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    # first_name = db.Column(db.String(120))
    # last_name = db.Column(db.String(120))
    # major = db.Column(db.String(120))
    # year = db.Column(db.Integer)
    # first_registration = db.Column(db.DateTime)

    def __repr__(self):
        return '<User %r>' % self.email
