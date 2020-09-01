import os
import requests
import urllib.parse

from flask import Flask, redirect, render_template, request
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/conference")
def conference():
    return render_template("conference.html")

@app.route("/calendar")
def calendar():
    return render_template("calendar.html")

@app.route("/resources", methods=["GET", "POST"])
def resources():
    if request.method=="GET":
        return render_template("resources.html")
    if request.method=="POST":
        if request.form.get("password") == "aquinas2019":
            return render_template("teachingresources.html")
        else:
            return render_template("invalid.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/studentwebsites")
def student_websites():
    return render_template("studentwebsites.html")

@app.route("/photoalbum")
def photo_album():
    return render_template("photoalbum.html")


