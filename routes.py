from app import app
from flask import render_template, url_for


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/sign-up")
def sign_up():
    return render_template("sign_up.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/add-post")
def add_post():
    return render_template("add_post.html")


@app.route("/admin")
def admin():
    return render_template("admin.html")

import routes