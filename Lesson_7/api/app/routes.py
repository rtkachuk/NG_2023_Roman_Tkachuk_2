from app import app, db
from app.models import Messages
from flask import request, redirect, make_response
import datetime
import sqlalchemy

@app.route('/send_message')
def send_message():
    username = request.args.get("username")
    message = request.args.get("message")

    db.session.add(Messages(userName=username, message=message, messageDate=datetime.datetime.now()))
    db.session.commit()

    return redirect('http://127.0.0.1:8080', code=302)

@app.route('/getAll')
def get_all():
    messages = Messages.query.all()
    data = ""
    for message in messages:
        data += "{}: {} [{}]<br>".format(message.userName, message.message, message.messageDate)
    responce = make_response(data)
    responce.headers['Access-Control-Allow-Origin'] = '*'
    return responce