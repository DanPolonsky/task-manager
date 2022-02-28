
from flask import request

from server import app
from server.route_handlers.authentication import login_handler, register_handler
from server.route_handlers.users.projects import project_creation_handler, project_deletion_handler
from server.utils.request_validation import token_required
from server.route_handlers.users.users import user_deletion_handler
from server.route_handlers.users.projects import project_list_handler


@app.route("/auth/login", methods = ["POST"])
def login():
    return login_handler(request)

@app.route("/auth/register", methods = ["POST"])
def register():
    return register_handler(request)


@app.route("/user/projects", methods = ["GET", "POST", "DELETE"])
@token_required
def project(user):
    if request.method == "GET":
        return project_list_handler(request, user)

    if request.method == "POST":
        return project_creation_handler(request, user)
    
    if request.method == "DELETE":
        return project_deletion_handler(request, user)


@app.route("/users", methods = ["DELETE"])
@token_required
def user_deletion(user):
    return user_deletion_handler(request, user)