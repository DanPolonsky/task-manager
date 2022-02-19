from server.utils.response import Response
from server.utils.db_functions import UserQueries
from server.utils.utils import hash_password

import re

## TODO: Add return jwt token on successful login or signup

def login_handler(request) -> Response:
    """ Function handles a login request using the request provided.

    Args:
        request (flask.request): The request object.

    Returns:
        Response: A reponse object.
    """

    try:
        data = request.json
        if not data:
            raise Exception()
    
    except Exception:
        return Response(success=False, data="request body must be in json format.", status_code=400)
    
    if "email" not in data or "password" not in data:
        return Response(success=False, data="missing email or password keys.", status_code=400)
    
    if not isinstance(data["email"], str) or not isinstance(data["password"], str):
        return Response(success=False, data="email(string) and/or password(string) types are not correct.", status_code=400)
    
    db_user = UserQueries.get_user_by_email(data["email"])

    if db_user:
        return Response(success=False, data="email doesnt exist.", status_code=401)
    

    if hash_password(data["password"]) != db_user.password:
        return Response(success=False, data="email or password are incorrect.", status_code=401)


    return Response(success=True, status_code=200)



def register_handler(request) -> Response:
    """ Function handles a register_handler request using the request provided.

    Args:
        request (flask.request): The request object.

    Returns:
        Response: A reponse object.
    """
    
    try:
        data = request.json
        if not data:
            raise Exception()
    
    except Exception:
        return Response(success=False, data="request body must be in json format.", status_code=400)

  
    if "email" not in data or "username" not in data or "password" not in data:
        return Response(success=False, data="missing email and/or password and/or username keys.", status_code=400)
    
    if not isinstance(data["email"], str) or not isinstance(data["password"], str) or not isinstance(data["username"], str):
        return Response(success=False, data="email(string) and/or username(string) and/or password(string) types are not correct.", status_code=400)
    
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if not re.fullmatch(email_regex, data["email"]):
        return Response(success=False, data="email is not in a correct format.", status_code=400)
    
    if len(data["password"]) < 6:
        return Response(success=False, data="password length must be above 6 characters.", status_code=400)
    
    if UserQueries.get_user_by_email(data["email"]):
        return Response(success=False, data="email already exists.", status_code=200)
    
    if UserQueries.get_user_by_username(data["username"]):
        return Response(success=False, data="username already exists.", status_code=200)
    
    
    UserQueries.create_user(data["email"], data["username"], data["password"])
    
    return Response(success=True, status_code=200)

