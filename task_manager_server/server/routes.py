from flask import request

from server import app
from server.route_handlers.authentication.authentication import login_handler, register_handler
from server.route_handlers.users.projects import project_creation_handler


### Temporary
from server.utils.db_functions import UserQueries
@app.after_request
def after_request(response):
    print(UserQueries.get_user_by_id(1))
    return response
####

@app.route('/auth/login', methods = ['POST'])
def login():
    return login_handler(request)

@app.route('/auth/register', methods = ['POST'])
def register():
    return register_handler(request)

@app.route("/users/project", methods = ['POST'])
def create_project():
    return project_creation_handler(request)