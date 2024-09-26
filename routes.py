from app import app
import users
import posts
from flask import session, render_template, flash, redirect, url_for
from forms import SignUpForm, LoginForm, PostForm, EditUserForm, CommentForm


@app.route("/")
def index():
    result = posts.get_posts()
    return render_template("index.html", posts = result)


@app.route("/add-post", methods=["GET", "POST"])
def add_post():
    form = PostForm()

    try:
        session["id"]
        logged_in = True
    except:
        logged_in = False

    if form.validate_on_submit():
        if logged_in:
            title = form.title.data
            content = form.title.data
            author = session["username"]
            author_id = session["id"]

            form.title.data = ""
            form.content.data = ""
            
            if not posts.add_post(title, content, author, author_id):
                flash("Error! Try Again")
                return render_template("add_post.html", form=form)
            else:
                flash("Post added Succesfully!")
                return redirect(url_for("index"))
        elif not logged_in:
            flash("Please login!")
    
    return render_template("add_post.html", form=form)

@app.route("/posts/<int:id>", methods=["GET", "POST"])
def post(id):
    form = CommentForm()
    result = posts.get_post(id)
    comments = posts.get_comments(id)

    if form.validate_on_submit():
        try:
            session["id"]
            logged_in = True
        except:
            logged_in = False
        if not logged_in:
            flash("You need to be logged in to comment...")
            return redirect(url_for("login"))

        content = form.content.data
        author_id = session["id"]
        post_id = id

        form.content.data = ""

        if not posts.add_comment(content, author_id, post_id):
            flash("Error! Try Again")
            return render_template("post", id=id, form=form, comments=comments)
        else:
            flash("Comment Added")
            render_template("post.html", post=result, form=form, comments=comments)

    return render_template("post.html", post=result, form=form, comments = comments)

@app.route("/edit-posts/<int:id>", methods=["GET", "POST"])
def edit_post(id):
    post_to_edit = posts.get_post(id)
    form = PostForm()

    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data

        form.title.data = ""
        form.content.data = ""

        if not posts.edit_post(id, title, content):
            flash("Error! Try Again")
            return render_template("add_post.html", form=form)
        else:
            flash("Post edited Succesfully!")
            return redirect(url_for("post", id=id))

    if post_to_edit.author_id == session["id"]:
        form.title.data = post_to_edit.title
        form.content.data = post_to_edit.content
        return render_template("edit_post.html", form=form)
    
    return render_template("edit_post.html", form=form)

@app.route("/delete-post/<int:id>")
def delete_post(id):
    post_to_delete = posts.get_post(id)

    if post_to_delete.author_id == session["id"]:
        if not posts.delete_post(id):
            flash("Error")
            return render_template("post", id=id)
        else:
            flash("Post Deleted") 
            return redirect("/")


@app.route("/dashboard")
def dashboard():
    try:
        id = session["id"]
        result = posts.get_user_posts(id)
    except:
        result = False
    return render_template("dashboard.html", posts=result)

@app.route("/dashboard/comments")
def comments():
    #placeholder
    comments = []
    return render_template("dashboard_comments.html", comments=comments)

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



"""@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_user(id):
    form = EditUserForm()
    user_to_update = users.get_user(id)
    form.username.data = user_to_update.username
    form.email.data = user_to_update.email

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data

        form.username.data = ""
        form.email.data = ""

        if not users.edit_user(id, username, email):
            flash("Error")
            return redirect(url_for("dashboard"))
        else:
            flash("You information was updated")
            return render_template("dashboard.html")


    return render_template("edit_user.html", form=form)"""