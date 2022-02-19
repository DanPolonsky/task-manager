from werkzeug.test import TestResponse
import logging

def print_response(response: TestResponse) :
    """ Function prints the response with the neccecary information. 

    Args:
        response (TestResponse): The server response.
    """      
    
    logging.debug(f"Response status code: {response.status_code}")
    logging.debug(f"Response headers: {response.headers._list}")
    logging.debug(f"Response json: {response.json}")
    


def response_is_valid(response: TestResponse, jwt_token=False) -> bool:
    """ Function checks if response is valid.

    Args:
        response (TestResponse): The server response.

    Returns:
        bool: True is response is valid.
    """
    return response.status_code == 200 and response.json["success"]
        