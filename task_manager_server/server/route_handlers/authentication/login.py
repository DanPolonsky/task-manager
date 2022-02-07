from server.utils.response import Response
from server.utils import db_functions


def login_handler(request) -> Response:
    """ Function handles a login request using the request provided.

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
        return Response(success=False, data="request body must be in json format.", status_code=400)
    
    if "email" not in data or "password" not in data:
        return Response(success=False, data="missing email or password keys.", status_code=400)
    
    if not isinstance(data["email"], str) or not isinstance(data["password"], str):
        return Response(success=False, data="email or password type are not a string.", status_code=400)
    
    if not db_functions.check_if_email_exists(data["email"]):
        return Response(success=False, data="email doesnt exist.", status_code=401)
    
    db_user = db_functions.get_user_by_email(data["email"])

    if db_functions.hash_password(data["password"]) != db_user.password:
        return Response(success=False, data="email or password are incorrect.", status_code=401)


    return Response(success=True, status_code=200)



