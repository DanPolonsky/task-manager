    
from functools import wraps

from flask import request
from server.properties import request_properties
from server.utils.db_functions import UserQueries
from server.utils.jwt_handler import JwtHandler
from server.utils.response import Response


def validate_request_data(request, parameters_types_dict):
    
    try:
        data = request.json
        if not data:
            raise Exception()
    
    except Exception:
        raise Exception("request body must be in json format.")

 

    missing_keys = False
    missing_keys_error = "missing: "
    for key in parameters_types_dict:
        if key not in data:
            missing_keys = True
            missing_keys_error += f"'{key}', "
   
       
    
    if missing_keys:  
        missing_keys_error = missing_keys_error[:-2]
        missing_keys_error += " keys."
        raise Exception(missing_keys_error)

    wrong_types = False
    wrong_types_error = "keys: "
    for key, value in parameters_types_dict.items():

        try:
            value(data[key])
        
        except Exception:
            wrong_types = True
            wrong_types_error += f"'{key}({value})', "
   
    
    
    if wrong_types:
        wrong_types_error = wrong_types_error[:-2]
        wrong_types_error += " types are not correct."
        raise Exception(wrong_types_error)

    return data



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

        if not UserQueries.get_user_by_id(user_id):
            return Response(success=False, data=f"Jwt token user doesnt exist anymore.", status_code=401)

        return f(user_id, *args, **kwargs)
    return decorator
