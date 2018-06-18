from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class LoginForm(FlaskForm):
    username = StringField("Käyttäjä", [validators.InputRequired()])
    password = PasswordField("Salasana", [validators.InputRequired()])

    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    name = StringField("Nimi")
    username = StringField("Käyttäjätunnus")
    password = PasswordField("Salasana")
    password2 = PasswordField("Toista salasana")

    class Meta:
        csrf = False
