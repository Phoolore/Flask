from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, EmailField, SelectField
from wtforms.validators import DataRequired, Length, Optional


class FeedbackForm(FlaskForm):
    name = StringField('name', validators=[Optional()])
    text = TextAreaField('feedback text', validators=[Optional()])
    email = EmailField('your email', validators=[Optional()])
    rating = SelectField("Your rate", choices = [i for i in range(1,11)])
    submit = SubmitField("Add")
    
    
class NewsForm(FlaskForm):
    title = StringField('title', validators=[DataRequired(message="Field is to be not empty")])
    text = TextAreaField('text', validators=[DataRequired(message="Field is to be not empty")])
    email = EmailField('your email', validators=[Optional()])
    submit = SubmitField("Add")