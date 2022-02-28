from server.models import UserPermissions
from server.utils.request_validation import validate_request_data
from server.utils.response import Response
from server.utils.db_functions import ProjectQueries, UserQueries
from server.properties import request_properties, response_properties




def project_creation_handler(request, user) -> Response:
    """ Function handles a project creation request using the request provided.

    Args:
        request (flask.request): The request object.

    Returns:
        Response: A reponse object.
    """
    
    try:
        data = validate_request_data(request, {
            request_properties.payload_keys.name: str,
            request_properties.payload_keys.description: str
        })

    except Exception as e:
        return Response(success=False, data=str(e), status_code=400)

    user_projects = UserQueries.get_user_projects(user)
    user_projects_names = [project.name for project in user_projects]
    

    if data[request_properties.payload_keys.name] in user_projects_names:
        return Response(success=False, data="project name already exists.", status_code=409)

    project = UserQueries.create_project(user, data[request_properties.payload_keys.name], data[request_properties.payload_keys.description])

    return Response(success=True, data={response_properties.payload_keys.project_id: project.id}, status_code=200)


def project_deletion_handler(request, user) -> Response:

    """ Function handles a project creation request using the request provided.

    Args:
        request (flask.request): The request object.

    Returns:
        Response: A reponse object.
    """
    
    try:
        data = validate_request_data(request, {
            request_properties.payload_keys.project_id: int,   
        })

    except Exception as e:
        return Response(success=False, data=str(e), status_code=400)

    project = ProjectQueries.get_project_by_id(data[request_properties.payload_keys.project_id])
    if not project:
        return Response(success=True, status_code=200)
    
    user_project_permission = UserQueries.get_user_project_permission(user, project)
    
    if user_project_permission != UserPermissions.OWNER:
        return Response(success=False, data=f"user doesnt have permission to delete project.", status_code=403)

    ProjectQueries.delete_project(project)

    return Response(success=True, status_code=200)


def project_list_handler(request, user):

    user_projects = UserQueries.get_user_projects(user)

    projects_response_dict = {
        response_properties.payload_keys.projects:[]
    }

    for project in user_projects:
        project_info = {}

        project_info["id"] = project.id
        project_info["name"] = project.name
        project_info["description"] = project.description

        projects_response_dict[response_properties.payload_keys.projects].append(project_info)

    return Response(success=True, data=projects_response_dict, status_code=200)
