from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class CategoryForm(FlaskForm):
    name = StringField("Kategorian nimi", [validators.InputRequired()])

    class Meta:
        csrf = False
