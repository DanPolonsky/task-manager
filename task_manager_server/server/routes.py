from flask import request

from server import app
from server.route_handlers.authentication.authentication import login_handler, register_handler
from server.route_handlers.users.projects import project_creation_handler



@app.route("/auth/login", methods = ["POST"])
def login():
    return login_handler(request)

@app.route("/auth/register", methods = ["POST"])
def register():
    return register_handler(request)

@app.route("/users/project", methods = ["POST"])
def create_project():
    return project_creation_handler(request)