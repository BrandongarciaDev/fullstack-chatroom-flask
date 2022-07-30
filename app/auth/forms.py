# absolute modules and libraries
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField, validators, ValidationError

# local modules and libraries
from .models import User


class Register(FlaskForm):
    username = StringField('Username', validators=[validators.DataRequired(), validators.Length(max=50)])
    email = EmailField('Email', validators=[validators.DataRequired()])
    password = PasswordField('Password', validators=[validators.DataRequired(),
                                                     validators.EqualTo('confirm_password')])
    confirm_password = PasswordField('Confirm password', validators=[validators.DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            print('Error email')
            raise ValidationError('This email is already in use')

    def validate_username(self, field):
        if User.query.filter_by(name=field.data).first():
            print('Error username')
            raise ValidationError('This username is already in user')


class Login(FlaskForm):
    email = EmailField('Email', validators=[validators.DataRequired()])
    password = PasswordField('Password', validators=[validators.DataRequired()])
    submit = SubmitField('Login')
