from sovellus import app, db
from flask import redirect, render_template, request, url_for
from sovellus.tehtavat.models import Tehtava

@app.route("/tehtavat/", methods=["GET"])
def tehtavat_index():
    return render_template("tehtavat/list.html", tehtavat = Tehtava.query.all())

@app.route("/tehtavat/new/")
def tehtavat_form():
    return render_template("tehtavat/new.html")

@app.route("/tehtava/<tehtava_id>/", methods=["POST"])
def tehtavat_set_done(tehtava_id):

    t = Tehtava.query.get(tehtava_id)
    if t.done == True:
        t.done = False
    else:
        t.done = True
    db.session().commit()

    return redirect(url_for("tehtavat_index"))

@app.route("/tehtava/<tehtava_id>/", methods=["POST"])
def tehtavat_delete():

    t = Tehtava(request.form.get("name"))
    
    db.session().delete(t)
    db.session().commit()

    return redirect(url_for("tehtavat_index"))

@app.route("/tehtavat/", methods=["POST"])
def tehtavat_create():
    t = Tehtava(request.form.get("name"))

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("tehtavat_index"))
