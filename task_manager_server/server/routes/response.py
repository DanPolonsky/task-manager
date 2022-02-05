
class Response:
    success: bool
    data: str|dict 

    def __new__(self, success, data=None):
        response = {"success": success}
        
        if data:
            response["data"] = data
        
        return response
