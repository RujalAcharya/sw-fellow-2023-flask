from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, IntegerField
from wtforms.validators import InputRequired

class TestForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    age = IntegerField('Age', validators=[InputRequired()])
    gender = RadioField('Gender', choices=['Male', 'Female', 'Others', 'Prefer not to say'], validators=[InputRequired()])



