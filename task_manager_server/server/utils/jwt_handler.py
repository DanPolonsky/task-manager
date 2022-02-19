import datetime
import jwt
from server import app

"""
    This module contains a list of jwt functions used by the server.
"""


class JwtHandler:

    def create_token(user_id: int) -> str:
        """ Function creates a jwt token with a payload of the user's id.

        Args:
            user_id (int): The user's id.

        Returns:
            str: The jwt token.
        """
        payload = {
            "user_id": user_id,
            "exp": datetime.datetime.now() + datetime.timedelta(hours=1)
        }
        
        jwt_token = jwt.encode(payload, app.config["SECRET_KEY"], algorithm=app.config["JWT_ALG"])
        return jwt_token
    

    def decode_token(token: str) -> int:
        """ Function decodes a user's jwt token.

        Args:
            token (str): The user's token.

        Returns:
            int: The user's id.
        """
        payload = jwt.decode(token, app.config["SECRET_KEY"], algorithm=app.config["JWT_ALG"])
        return payload["user_id"]