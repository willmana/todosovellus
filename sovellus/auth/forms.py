from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class LoginForm(FlaskForm):
    username = StringField("Käyttäjä", [validators.InputRequired(), validators.Length(max=144)])
    password = PasswordField("Salasana", [validators.InputRequired(), validators.Length(max=144)])

    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(max=144)])
    username = StringField("Käyttäjätunnus", [validators.Length(max=144)])
    password = PasswordField("Salasana", [validators.Length(max=144)])
    password2 = PasswordField("Toista salasana", [validators.Length(max=144)])

    class Meta:
        csrf = False
