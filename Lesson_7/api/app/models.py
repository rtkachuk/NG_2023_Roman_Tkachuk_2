from app import db

class Messages(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    userName = db.Column(db.String(256))
    message = db.Column(db.String(256))
    messageDate = db.Column(db.DateTime)