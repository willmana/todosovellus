from flask import render_template
from sovellus import app
from sovellus.auth.models import User

@app.route("/")
def index():
    return render_template("index.html")
