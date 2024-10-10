from app import app
import users
import posts
import comments
from flask import session, render_template, flash, redirect, url_for
from forms import SearchForm, SignUpForm, LoginForm, PostForm, EditUserForm, CommentForm

@app.route("/")
def index():
    result = posts.get_posts()
    return render_template("index.html", posts = result)

@app.context_processor
def base():
    form = SearchForm()
    return dict(form=form)

@app.route("/search", methods=["POST", "GET"])
def search():
    form = SearchForm()

    if form.validate_on_submit():
        searched = form.search.data
        result = posts.get_searched_posts(searched)
        count= len(result)

        return render_template("search.html", form=form, searched=searched, count=count, posts=result)

@app.route("/search/users", methods=["POST", "GET"])
def search_users():
    form = SearchForm()

    if form.validate_on_submit():
            searched = form.search.data
            result = users.get_searched_user(searched)
            count= len(result)

    return render_template("search_users.html", form=form, searched=searched, count=count, users=result)

@app.route("/search/posts", methods=["POST", "GET"])
def search_posts():
    form = SearchForm()

    if form.validate_on_submit():
            searched = form.search.data
            result = posts.get_searched_posts_id(searched)
            count = len(result)

    return render_template("search_posts.html", form=form, searched=searched, count= count, posts=result)


@app.route("/add-post", methods=["GET", "POST"])
def add_post():
    form = PostForm()

    if form.validate_on_submit():
        if users.is_logged_in():
            title = form.title.data
            content = form.title.data
            author_id = session["id"]

            form.title.data = ""
            form.content.data = ""
            
            if not posts.add_post(title, content, author_id):
                flash("Error! Try Again")
                return render_template("add_post.html", form=form)
            else:
                flash("Post added Succesfully!")
                return redirect(url_for("index"))
        else:
            flash("You need to be logged in to make posts...")
            return redirect(url_for('login'))
    
    return render_template("add_post.html", form=form)

@app.route("/posts/<int:id>", methods=["GET", "POST"])
def post(id):
    form = CommentForm()
    result = posts.get_post(id)
    post_comments = comments.get_comments(id)

    if form.validate_on_submit():
        if not users.is_logged_in():
            flash("You need to be logged in to make comments...")
            return redirect(url_for("login"))
        else:
            content = form.content.data
            author_id = session["id"]
            post_id = id
            form.content.data = ""

            if not comments.add_comment(content, author_id, post_id):
                flash("Error! Try Again")
                return render_template("post", id=id, form=form, comments=post_comments)
            else:
                flash("Comment Added")
                post_comments = comments.get_comments(id)
                render_template("post.html", post=result, form=form, comments=post_comments)

    return render_template("post.html", post=result, form=form, comments=post_comments)

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

    if post_to_delete.author_id == session["id"] or session["role"] == "administrator":
        if not posts.delete_post(id):
            flash("Error")
            return render_template("post", id=id)
        else:
            flash("Post Deleted") 
            if session["role"] == "administrator":
                return redirect(url_for("admin_posts"))
            return redirect("/")

@app.route("/delete-comment/<int:id>")
def delete_comment(id):
    comment_to_delete = comments.get_comment(id)

    if comment_to_delete.author_id == session["id"] or session["role"] == "administrator":
        if not comments.delete_comment(id):
            flash("Error")
            return render_template("post", id=id)
        else:
            flash("Comment Deleted") 
            return redirect(url_for("post", id=comment_to_delete.post_id))

@app.route("/dashboard")
def dashboard():
    try:
        id = session["id"]
        result = posts.get_user_posts(id)
    except:
        result = False
        flash("You need to br logged in to view this page...")
    return render_template("dashboard.html", posts=result)

@app.route("/dashboard/comments")
def user_comments():
    try:
        id = session["id"]
        result = comments.get_user_comments(id)
    except:
        result = False
    return render_template("dashboard_comments.html", comments=result)

@app.route("/admin")
def admin():
    form = SearchForm()

    if not users.is_logged_in():
        flash("Please log in to view this page")
        return redirect(url_for("login"))
    
    if session["role"] == "administrator":
        if form.validate_on_submit():
            searched = form.search.data
            result = users.get_searched_user(searched)
            return redirect("search/users.html", form=form, searched=searched, users=result)
    
        result = users.get_users()
        return render_template("admin.html", users=result)

    flash("Access Denied")
    return redirect(url_for("index"))

@app.route("/admin/posts")
def admin_posts():
    form = SearchForm()

    if session["role"] == "administrator":
        result = posts.get_posts()
        return render_template("admin_posts.html", posts=result)
    
    if session["role"] == "administrator":
        if form.validate_on_submit():
            searched = form.search.data
            result = posts.get_searched_posts_id(searched)
            return redirect("search/posts.html", form=form, searched=searched, posts=result)
    
    flash("Access Denied")
    return redirect(url_for("index"))

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        form.email.data = ""
        form.password.data = ""

        if users.check_email(email):
            flash('We could not find an account with this email.')

        elif not users.login(email, password):
            flash('Wrong Password')
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

        if not users.check_email(email):
            flash("Email already in use")
            return render_template("sign_up.html", form=form)
        if not users.signup(username, email, password):
            flash("Error! Try Again")
            return render_template("sign_up.html", form=form)
        else:
            flash("Welcome! You are now logged in and ready to start posting.")
            return redirect(url_for("dashboard"))
    
    return render_template("sign_up.html", form=form)

@app.route("/profile/<int:id>")
def profile(id):
    user = users.get_user(id)
    user_posts = posts.get_user_posts(id)
    return render_template("profile.html", user=user, posts=user_posts)

@app.route("/profile/comments/<int:id>")
def profile_comments(id):
    user = users.get_user(id)
    user_comments = comments.get_user_comments(id)
    return render_template("profile_comments.html", user=user, comments=user_comments)

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_user(id):
    form = EditUserForm()
    user = users.get_user(id)

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        bio = form.bio.data

        form.username.data = ""
        form.email.data = ""
        form.bio.data = ""

        if not users.edit_user(id, username, email, bio):
            flash("Error")
            return redirect(url_for("dashboard"))
        else:
            flash("You information was updated")
            return redirect(url_for("dashboard"))
        
    if id == session["id"]:
        form.username.data = user.username
        form.email.data = user.email
        form.bio.data = user.bio
        return render_template("edit_user.html", form=form)
    else:
        flash("Unauthorized Access")
        return redirect(url_for('index'))

@app.route("/delete-user/<int:id>")
def delete_user(id):
    user_to_delete = users.get_user(id)

    if user_to_delete.id == session["id"] or session["role"] == "administrator":
        if not users.delete_user(id):
            flash("Error")
            if session["role"] == "administrator":
                return redirect(url_for("admin"))
            return redirect(url_for("dashboard"))
        else:
            flash("User deleted successfully") 
            if session["role"] == "administrator":
                return redirect(url_for("admin"))
            return redirect(url_for("sign_up"))

@app.route("/follow/<int:id>")
def follow(id):
    followed_id= id
    if not users.is_logged_in():
        flash('Please log in first')
        return redirect(url_for('login'))
    else:
        if not users.follow(followed_id):
            flash("Error")
            return redirect(url_for('profile', id=followed_id))

    return redirect(url_for('profile', id=followed_id))

@app.route("/unfollow/<int:id>")
def unfollow(id):
    followed_id= id

    if not users.is_logged_in():
        flash('Please log in first')
        return redirect(url_for('login'))
    else:
        if not users.unfollow(followed_id):
            flash("Error")
            return redirect(url_for('profile', id=followed_id))     
    return redirect(url_for('dashboard'))

@app.route("/followed-accounts/<int:id>")
def followed_accounts(id):
    if not users.is_logged_in():
        flash("Please log in to view this page")
        return redirect(url_for('login'))
    if session["id"] == id:
        accounts = users.followed_accounts(id)
        post = posts.get_followed_posts(id)
        return render_template("followed.html", accounts=accounts, posts=post)
    else:
        flash("Unauthorized access")
        return redirect(url_for('dashboard'))