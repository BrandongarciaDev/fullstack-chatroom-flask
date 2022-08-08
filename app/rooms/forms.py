from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField, TextAreaField
from flask_wtf.file import FileField, FileRequired
from wtforms.validators import DataRequired
from flask import current_app
from .models import Category



class CreateRoom(FlaskForm):
    title = StringField('Chatroom title', validators=[DataRequired()])
    image = FileField("Upload chatroom image")
    description = TextAreaField('description', validators=[DataRequired()])
    rooms_types = RadioField(choices=[('Chatroom wil be public', 'public'), ('value2', 'private')])
    category = RadioField()

    submit = SubmitField('Create chatroom')


