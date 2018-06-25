from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user, login_manager

from sovellus import app, db
from sovellus.tehtavat.models import Tehtava
from sovellus.tehtavat.forms import TaskForm, ModifyForm
from sovellus.kategorialuokat.models import Kategoria


@app.route("/tehtavat/", methods=["GET"])
@login_required
def tehtavat_index():
    return render_template("tehtavat/list.html", tehtavat = Tehtava.tasks_by_account(current_user.id))

@app.route("/tehtavat/new/")
@login_required
def tehtavat_form():
    categories = Kategoria.categories_by_user(current_user.id)
    form = TaskForm()
    form.category.choices = categories
    return render_template("tehtavat/new.html", form = form)

@app.route("/tehtava/<tehtava_id>/", methods=["POST"])
@login_required
def tehtavat_set_done(tehtava_id):

    t = Tehtava.query.get(tehtava_id)
    if t.done == True:
        t.done = False
    else:
        t.done = True
    db.session().commit()

    return redirect(url_for("tehtavat_index"))

@app.route("/tehtava/poista/<tehtava_id>/", methods=["POST"])
@login_required
def tehtavat_delete(tehtava_id):

    t = Tehtava.query.get(tehtava_id)

    db.session().delete(t)
    db.session().commit()

    return redirect(url_for("tehtavat_index"))

@app.route("/tehtavat/", methods=["POST"])
@login_required
def tehtavat_create():
    form = TaskForm(request.form)
    form.category.choices = Kategoria.categories_by_user(current_user.id)

    if not form.validate():
        return render_template("tehtavat/new.html", form = form)

    t = Tehtava(form.name.data, Kategoria.all_by_id(form.category.data), form.importance.data)
    t.done = form.done.data
    t.account_id = current_user.id

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("tehtavat_index"))

@app.route("/tehtavat/infosivu/<tehtava_id>/", methods=["POST"])
@login_required
def tehtavat_open(tehtava_id):
    t = Tehtava.query.get(tehtava_id)
    return render_template("tehtavat/infosivu.html", tehtava = t)

@app.route("/tehtavat/muokkaa/<tehtava_id>/", methods=["POST"])
@login_required
def tehtavat_muokkaa(tehtava_id):
    t = Tehtava.query.get(tehtava_id)
    return render_template("tehtavat/muokkaus.html", tehtava = t, form = ModifyForm())

@app.route("/tehtavat/muokkaa/hyvaksy/<tehtava_id>/", methods=["POST"])
@login_required
def hyvaksy_muutokset(tehtava_id):
    form = ModifyForm(request.form)
    t = Tehtava.query.get(tehtava_id)

    if not form.validate():
        return render_template("tehtavat/muokkaus.html", tehtava = t, form = ModifyForm())



    t.name = form.name.data
    t.done = form.done.data
    t.importance = form.importance.data



    db.session().commit()

    return render_template("tehtavat/infosivu.html/", tehtava = t)
