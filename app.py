# This is a sample Python script.

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("resume_isaac.html")
