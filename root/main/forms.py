from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, length, Email


class AddNewAccountForm(FlaskForm):
    account_name = StringField('Account Name', validators=[length(1,20), DataRequired()])
    description = StringField('Description (optional)', validators=[length(0,40)])
    email = StringField('Email', validators=[DataRequired(), Email(), length(1, 40)])
    username = StringField('Username (optional)', validators=[length(0,20)])
    password_hint = StringField('Password hint (optional)', validators=[length(0,40)])
    submit = SubmitField('Add account')