from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, TextAreaField 
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError

class MessageForm(FlaskForm):
    name = StringField(label='name:', validators=[Length(min=2, max=30), DataRequired()])
    date = DateTimeField(label='date:')
    description = TextAreaField(label='description:', validators=[DataRequired()])


class OwnerForm(FlaskForm):
    code = StringField(label='code: ', validators=[Length(min=1, max=8), DataRequired()])