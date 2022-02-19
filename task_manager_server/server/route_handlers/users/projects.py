from server.utils.response import Response
from server.utils.db_functions import UserQueries
from server.properties import request_properties, response_properties

def project_creation_handler(request, user_id) -> Response:
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

    if request_properties.payload_keys.name not in data or request_properties.payload_keys.description not in data:
        return Response(success=False, data="missing 'name' and/or 'description' key.", status_code=400)
    
    if not isinstance(data[request_properties.payload_keys.name], str) or not isinstance(data[request_properties.payload_keys.description], str):
        return Response(success=False, data="name(string) and/or description(string) types are not correct.", status_code=400)

    user_projects = UserQueries.get_user_projects(user_id)
    user_projects_names = [project.name for project in user_projects]
    

    if data[request_properties.payload_keys.name] in user_projects_names:
        return Response(success=False, data="project name already exists.", status_code=200)

    project = UserQueries.create_project(user_id, data[request_properties.payload_keys.name])

    return Response(success=True, data={response_properties.payload_keys.project_id: project.id}, status_code=200)