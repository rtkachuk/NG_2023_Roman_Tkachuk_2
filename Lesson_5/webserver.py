from flask import Flask, render_template, request

servak = Flask("Lesson_5")

@servak.route("/")
def index():
    return render_template("index.html", data="TEST")

@servak.route("/ask")
def ask():
    return render_template("ask.html")

@servak.route("/sum")
def sum():
    firstValue = float(request.args.get("valuea"))
    secondValue = float(request.args.get("valueb"))
    return str(firstValue + secondValue)

servak.run(host="0.0.0.0", port=8080)