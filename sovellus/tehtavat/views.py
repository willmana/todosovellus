from flask import redirect, render_template, request, url_for
from flask_login import login_required

from sovellus import app, db
from sovellus.tehtavat.models import Tehtava
from sovellus.tehtavat.forms import TaskForm


@app.route("/tehtavat/", methods=["GET"])
def tehtavat_index():
    return render_template("tehtavat/list.html", tehtavat = Tehtava.query.all())

@app.route("/tehtavat/new/")
@login_required
def tehtavat_form():
    return render_template("tehtavat/new.html")

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

    if not form.validate():
        return render_template("tehtavat/new.html", form = form)

    t = Tehtava(form.name.data)
    t.done = form.done.data
    t.account_id = current_user.id

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("tehtavat_index"))
