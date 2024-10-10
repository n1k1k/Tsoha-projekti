from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError
from wtforms.validators import DataRequired, EqualTo, Length
from wtforms.widgets import TextArea

class SignUpForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(max=35)])
    email = StringField("Email", validators=[DataRequired(), Length(max=200)])
    password = PasswordField("Password", validators=[DataRequired(), Length(max=300), EqualTo('confirm_password', message="Passwords do not match")])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired()])
    submit = SubmitField("Sign Up")

class EditUserForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(max=35)])
    email = StringField("Email", validators=[DataRequired(), Length(max=200)])
    bio = StringField("Bio", widget=TextArea(), validators=[Length(max=500)])
    submit = SubmitField("Submit")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(100)])
    content = StringField("Content", validators=[DataRequired(), Length(2500)], widget=TextArea())
    submit = SubmitField("Post")

class CommentForm(FlaskForm):
    content = StringField("Content", validators=[DataRequired(), Length(1000)], widget=TextArea())
    submit = SubmitField("Submit")

class SearchForm(FlaskForm):
    search = StringField("Search", validators=[Length(2500)])
    submit = SubmitField("Search")