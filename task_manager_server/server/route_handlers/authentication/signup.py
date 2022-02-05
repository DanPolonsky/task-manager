
from server.route_handlers.response import Response
import re

from server import db_functions


def signup_handler(request) -> Response:
    """ Function handles a signup request using the request provided.

    Args:
        request (flask.request): The request object.

    Returns:
        [Response]: A reponse object.
    """
    
    try:
        data = request.json
        if not data:
            raise Exception()
    
    except Exception:
        return Response(success=False, data="request body must be in json format.")

  
    if "email" not in data or "username" not in data or "password" not in data:
        return Response(success=False, data="missing email or password keys.")
    
    if not isinstance(data["email"], str) or not isinstance(data["password"], str) or not isinstance(data["username"], str):
        return Response(success=False, data="email, username or password types are not string.")
    
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if not re.fullmatch(email_regex, data["email"]):
        return Response(success=False, data="email is not in a correct format.")
    
    if len(data["password"]) < 6:
        return Response(success=False, data="password length must be above 6 characters.")
    
    if db_functions.check_if_email_exists(data["email"]):
        return Response(success=False, data="email already exists.")
    
    if db_functions.check_if_username_exists(data["username"]):
        return Response(success=False, data="username already exists.")
    
    db_functions.create_user(data["email"], data["username"], data["password"])
    
    return Response(success=True)