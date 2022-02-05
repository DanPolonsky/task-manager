from server.route_handlers.response import Response


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
        return Response(success=False, data="request body must be in json format.")
    
    if "email" not in data or "password" not in data:
        return Response(success=False, data="missing email or password keys.")
    
    if not isinstance(data["email"], str) or not isinstance(data["password"], str):
        return Response(success=False, data="email or password type are not string.")
    
    return Response(success=True)



