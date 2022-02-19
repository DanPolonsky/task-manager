from functools import wraps
from flask import request

from server import app
from server.route_handlers.authentication.authentication import login_handler, register_handler
from server.route_handlers.users.projects import project_creation_handler
from server.utils.response import Response
from server.utils.jwt_handler import JwtHandler
from server.properties import request_properties

def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):

        token = None

        if request_properties.header_keys.authrorization not in request.headers:
            return Response(success=False, data="Missing Authorization header containing jwt token.", status_code=401)

        autherization_header = request.headers[request_properties.header_keys.authrorization]
        autherization_header_parts = autherization_header.split()
        
        if len(autherization_header_parts) != 2:
            return Response(success=False, data="Authorization header value in a wrong format: 'Bearer <token>'.", status_code=401)

        if autherization_header_parts[0] != request_properties.header_values.bearer:
            return Response(success=False, data="Missing Authorization Bearer key word in Authorization header.", status_code=401)
        

        token = autherization_header_parts[1]

        try:
            user_id = JwtHandler.decode_token(token)
        
        except Exception as e:
            return Response(success=False, data=f"Error decoding jwt token: {str(e)}.", status_code=401)

        return f(user_id, *args, **kwargs)
    return decorator


@app.route("/auth/login", methods = ["POST"])
def login():
    return login_handler(request)

@app.route("/auth/register", methods = ["POST"])
def register():
    return register_handler(request)

@app.route("/users/project", methods = ["POST"])
@token_required
def create_project(user_id):
    return project_creation_handler(request, user_id)