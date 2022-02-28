import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

config = os.environ.get("CONFIG") 

app.config.from_object(config)


db = SQLAlchemy(app)


import server.routes
import server.models

# Clearing database if testing flag is active
if app.config["TESTING"]:
    db.drop_all()


db.create_all()
