from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SECRET_KEY"] = "some-secret"

db = SQLAlchemy(app)


import server.routes
import server.models


if not db.engine.table_names():
    db.create_all()


