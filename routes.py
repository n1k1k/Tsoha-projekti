from app import app
import users
from flask import render_template, flash, redirect, url_for
from forms import SignUpForm, LoginForm, PostForm
from werkzeug.security import generate_password_hash


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add-post", methods=["GET", "POST"])
def add_post():
    form = PostForm()
    title = None
    content = None

    if form.validate_on_submit():

        #testing form
        title = form.title.data
        content = form.content.data

        #clear data
        form.title.data = ""
        form.content.data = ""
    
    return render_template("add_post.html", form=form, title=title, content=content)

@app.route("/post")
def post():
    return render_template("post.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        form.email.data = ""
        form.password.data = ""

        if not users.login(email, password):
            flash('Something went wrong. Try Again!')
        else:
            return redirect(url_for('dashboard'))

    
    return render_template("login.html", form=form)

@app.route("/logout", methods=["GET", "POST"])
def logout():
    users.logout()
    flash("You have been Logged out!")
    return redirect(url_for("login"))

@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    username = None
    form = SignUpForm()

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        form.username.data = ""
        form.email.data = ""
        form.password.data = ""

        if not users.signup(username, email, password):
            flash("Error! Try Again")
            return render_template("sign_up.html", form=form)
        else:
            flash("Welcome! You are now logged in and ready to start posting.")
            return redirect(url_for("dashboard"))
    
    return render_template("sign_up.html", form=form)



@app.route("/edit", methods=["GET", "POST"])
def edit_user():
    form = SignUpForm()

    #check user

    if form.validate_on_submit():
        #Add data to db

        #clear data
        form.username.data = ""
        form.email.data = ""

    

    return render_template("edit_user.html", form=form)