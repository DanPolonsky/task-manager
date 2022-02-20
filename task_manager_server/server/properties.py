
class request_properties:
    class payload_keys:
        username = "username"
        email = "email"
        password = "password"
        name = "name"
        description = "description"
        project_id = "project_id"
    
    class header_keys:
        authrorization = "Authorization"
    
    class header_values:
        bearer = "Bearer"



class response_properties:
    class payload_keys:
        data = "data"
        token = "token"
        project_id = "project_id"



class jwt_properties:
    class payload_keys:
        user_id = "user_id"
        exp = "exp"
    
    experation_time = 60 # minutes
