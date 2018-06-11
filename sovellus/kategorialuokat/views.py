from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from sovellus import app, db
from sovellus.kategorialuokat.models import Kategoria
from sovellus.kategorialuokat.forms import CategoryForm

@app.route("/kategoriat/", methods=["GET"])
def categories_index():
   return render_template("kategoriat/list.html", categories = Kategoria.query.all())



@app.route("/kategoriat/new/")
@login_required
def categories_form():
    return render_template("kategoriat/new.html", form = CategoryForm(), categories = Kategoria.query.all())

@app.route("/kategoriat/delete/<category_id>/", methods=["POST"])
@login_required
def categories_delete(category_id):

    c = Kategoria.query.get(category_id)
    if c.account_id != current_user.id:
        return login_manager.unauthorized()

    db.session().delete(c)
    db.session().commit()

    return redirect(url_for("categories_index"))

@app.route("/kategoriat/", methods=["POST"])
@login_required
def categories_create():
    form = CategoryForm(request.form)

    if not form.validate():
        return render_template("kategoriat/new.html", form = form)

    c = Kategoria(form.name.data)

    c.account_id = current_user.id

    db.session().add(c)
    db.session().commit()

    return redirect(url_for("categories_index"))
