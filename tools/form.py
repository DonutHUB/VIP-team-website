from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
from wtforms.widgets import TextArea

class ContactForm(FlaskForm):
    first = StringField('First Name', validators=[DataRequired()])
    last = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Your Email', validators=[DataRequired(), Email()])
    body = StringField(u'Message', widget=TextArea())
    submit = SubmitField('Send Message!')