from app import app, db
from app.models import Users
from flask import request, redirect
import sqlalchemy

@app.route('/')
def index():
    return "Hello world"

@app.route('/add-user')
def addUser():
    dataUsername = request.args.get("username")
    db.session.add(Users(username = dataUsername))
    db.session.commit()
    return redirect("/get-users", code=302)


@app.route('/get-users')
def getUsers():
    responce = []
    users = Users.query.all()
    for user in users:
        responce.append(user.username)
    return responce

@app.route('/get-user')
def getUser():
    answer = []
    dataUsername = request.args.get("username")
    try:
        #sql = sqlalchemy.select('*').where(Users.username == dataUsername)
        sql = sqlalchemy.text("SELECT * FROM Users WHERE username='{}';".format(dataUsername))
        print(sql)
        for user in db.session.execute(sql):
            answer.append(str(user))
        return "".join(answer)
    except Exception as e:
        return "ERROR: {}".format(str(e))