from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators, SelectMultipleField, IntegerField
from wtforms.validators import InputRequired

class TaskForm(FlaskForm):
    name = StringField("Tehtävän nimi", [validators.Length(min=3), validators.InputRequired(), validators.Length(max=144)])
    category = SelectMultipleField("Kategoria", coerce=int, validators=[InputRequired()])
    importance = IntegerField("Kiireellisyys välillä 1-10", [validators.NumberRange(min=1, max=10, message = "Tulee olla väliltä 1-10")])
    done = BooleanField("Suoritettu")

    class Meta:
        csrf = False

class ModifyForm(FlaskForm):
    name = StringField("Tehtävän nimi", [validators.Length(min=3), validators.InputRequired(), validators.Length(max=144)])
    importance = IntegerField("Kiireellisyys välillä 1-10", [validators.NumberRange(min=1, max=10, message="Tulee olla väliltä 1-10")])
    done = BooleanField("Suoritettu")

    class Meta:
        csrf = False
