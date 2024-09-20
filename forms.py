from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError
from wtforms.validators import DataRequired, EqualTo, Length
from wtforms.widgets import TextArea

class SignUpForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), EqualTo('confirm_password', message="Passwords do not match")])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired()])
    submit = SubmitField("Submit")



class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), EqualTo('confirm_password_hash', message="Passwords do not match")])
    submit = SubmitField("Login")

class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content = StringField("Content", validators=[DataRequired()], widget=TextArea())
    submit = SubmitField("Post")
