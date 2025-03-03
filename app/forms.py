from flask_wtf import FlaskForm
from wtforms import EmailField, StringField, TextAreaField
from wtforms.validators import DataRequired


class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired()])
    subject = StringField("Subject", validators=[DataRequired()])
    message = TextAreaField("Message", validators=[DataRequired()])
