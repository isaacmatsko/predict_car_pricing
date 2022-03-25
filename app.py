# This is a sample Python script.

from flask import Flask, render_template

app = Flask(__name__)



@app.route("/")
def Welcomepage():
    return render_template(
        title=
        body=

    )

@app.route("/about")
def projectwriteup():



@app.route("/isaac")
def issac():
    return render_template("resume_isaac.html")

@app.route("/sean")
def sean():
    return render_template("resume_sean.html")

@app.route("/alec")
def alec():
    return render_template("resume_alec.html")

@app.route("/shane")
def shane():
    return render_template("resume_shane.html")


