from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators, SelectMultipleField

class TaskForm(FlaskForm):
    name = StringField("Tehtävän nimi", [validators.Length(min=3), validators.InputRequired(), validators.Length(max=144)])
    category = SelectMultipleField("Kategoria", coerce=int)
    done = BooleanField("Suoritettu")

    class Meta:
        csrf = False
