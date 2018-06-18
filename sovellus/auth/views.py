from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from sovellus import app, db
from sovellus.auth.models import User
from sovellus.auth.forms import LoginForm, RegisterForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/login.html", form = LoginForm())

    form = LoginForm(request.form)


    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/login.html", form = form,
                               error = "No such username or password")


    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/")
def auth_form():
    return  render_template("auth/register.html", form = RegisterForm())

@app.route("/auth/", methods = ["POST"])
def auth_create():
    form = RegisterForm(request.form)

    if not form.validate():
        print("Vikatikki1")
        return render_template("auth/register.html", form = form)
    if not form.password.data == form.password.data:
        print("Vikatikki2")
        return render_template("auth/register.html", form = form)

    k = User(form.name.data, form.username.data, form.password.data)


    db.session().add(k)
    db.session().commit()

    return render_template("auth/login.html", form = RegisterForm())
