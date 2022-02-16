import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(os.environ["CONFIG"])

db = SQLAlchemy(app)


import server.routes
import server.models

# Clearing database if testing flag is active
if app.config["TESTING"]:
    db.drop_all()


if not db.engine.table_names():
    db.create_all()
