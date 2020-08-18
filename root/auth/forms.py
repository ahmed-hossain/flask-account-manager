from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, length


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(),length(max=20)])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me')
    submit = SubmitField('submit')