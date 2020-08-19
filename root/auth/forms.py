from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, length, EqualTo, Email
from wtforms import ValidationError
from root.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),length(max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember_me')
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),length(max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_2 = PasswordField(
        'Confirm password', validators=[DataRequired(),
        EqualTo('password', message="Passwords didn't match" )])
    submit = SubmitField('Create Account')

    def validate_username(self, username):
        if User.query.filter_by(username=username.data).first():
            raise ValueError('Username is already taken.')
    
    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValueError('This email is already used.')