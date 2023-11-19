from app import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique = True)
    password = db.Column(db.String(256))

class Messages(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    userId = db.Column(db.Integer)
    message = db.Column(db.String(256))
    messageDate = db.Column(db.DateTime)