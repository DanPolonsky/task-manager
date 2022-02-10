from server.utils.response import Response
from server.utils.db_functions import UserQueries


def project_creation_handler(request) -> Response:
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
        return Response(success=False, data="request body must be in json format.", status_code=400)

  
    if "email" not in data or "username" not in data or "password" not in data:
        return Response(success=False, data="missing email and/or password and/or username keys.", status_code=400)
    
    if not isinstance(data["email"], str) or not isinstance(data["password"], str) or not isinstance(data["username"], str):
        return Response(success=False, data="email, username or password types are not string.", status_code=400)
    
    
    
    return Response(success=True, status_code=200)