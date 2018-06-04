from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tehtavat.db"
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

from sovellus import views

from sovellus.tehtavat import models
from sovellus.tehtavat import views

from sovellus.auth import models

db.create_all()
