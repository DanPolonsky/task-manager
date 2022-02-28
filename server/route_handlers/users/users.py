

from server.utils.request_validation import validate_request_data
from server.properties import request_properties
from server.utils.response import Response
from server.utils.db_functions import UserQueries


def user_deletion_handler(request, user):
    UserQueries.delete_user(user)
    
    return Response(success=True, status_code=200)