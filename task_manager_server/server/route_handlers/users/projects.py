from server.utils.response import Response
from server.utils.db_functions import UserQueries


def project_creation_handler(request) -> Response:
    """ Function handles a project creation request using the request provided.

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

    if "name" not in data or "description" not in data:
        return Response(success=False, data="missing 'name' and/or 'description' key.", status_code=400)
    
    if not isinstance(data["name"], str) or not isinstance(data["description"], str):
        return Response(success=False, data="name(string) and/or description(string) types are not correct.", status_code=400)

    # TODO: check user id in jwt token instead of static user id    
    user_id = 1

    user_projects = UserQueries.get_user_projects(user_id)
    user_projects_names = [project.name for project in user_projects]
    

    if data["name"] in user_projects_names:
        return Response(success=False, data="project name already exists.", status_code=200)

    UserQueries.create_project(user_id, data["name"])

    return Response(success=True, status_code=200)