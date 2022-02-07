class Response:
    """ This class represents a response from the server.

    Returns:
        [type]: [description]
    """
    success: bool
    data: dict 

    def __new__(self, success, status_code, data=None) -> tuple:
        response_body = {"success": success}
        
        if data:
            response_body["data"] = data
        
        return response_body, status_code
