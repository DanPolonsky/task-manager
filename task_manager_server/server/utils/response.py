
class Response:
    success: bool
    data: str|dict 

    def __new__(self, success, status_code, data=None):
        response_body = {"success": success}
        
        if data:
            response_body["data"] = data
        
        return response_body, status_code
