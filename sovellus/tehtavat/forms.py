from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators

class TaskForm(FlaskForm):
    name = StringField("Tehtävän nimi", [validators.Length(min=3), validators.InputRequired()])
    done = BooleanField("Suoritettu")

    class Meta:
        csrf = False
