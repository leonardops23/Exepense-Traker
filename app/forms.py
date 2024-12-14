from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from .models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already registered')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class TrackerForm(FlaskForm):
    name = StringField('Tracker Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    submit = SubmitField('Create Tracker')

class TrackerEntryForm(FlaskForm):
    value = FloatField('Value', validators=[DataRequired()])
    note = TextAreaField('Note')
    submit = SubmitField('Add Entry')
