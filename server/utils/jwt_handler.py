import datetime
import jwt

from server import app
from server.models import User
from server.properties import jwt_properties

class JwtHandler:

    def create_token(user_id: int) -> str:
        """ Function creates a jwt token with a payload of the user's id.

        Args:
            user_id (int): The user's id.

        Returns:
            str: The jwt token.
        """
        payload = {
            jwt_properties.payload_keys.user_id: user_id,
            jwt_properties.payload_keys.exp: datetime.datetime.now() + datetime.timedelta(jwt_properties.experation_time)
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
        payload = jwt.decode(token, app.config["SECRET_KEY"], algorithms=[app.config["JWT_ALG"]])
        return payload[jwt_properties.payload_keys.user_id]
