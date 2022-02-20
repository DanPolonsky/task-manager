
from flask import request

from server import app
from server.route_handlers.authentication import login_handler, register_handler
from server.route_handlers.users.projects import project_creation_handler, project_deletion_handler
from server.utils.request_validation import token_required


### FOR DEBUGGING
@app.after_request
def after_request_func(response):
    from server.models import User, UserProjectAssociation, Project
    print(User.query.all())
    print(UserProjectAssociation.query.all())
    print(Project.query.all())

    return response



@app.route("/auth/login", methods = ["POST"])
def login():
    return login_handler(request)

@app.route("/auth/register", methods = ["POST"])
def register():
    return register_handler(request)

@app.route("/user/projects", methods = ["POST", "DELETE"])
@token_required
def create_project(user_id):
    if request.method == "POST":
        return project_creation_handler(request, user_id)
    
    if request.method == "DELETE":
        return project_deletion_handler(request, user_id)