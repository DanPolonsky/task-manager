import jwt

from server import app
from server.models import User


class JwtHandler:
    """
        This static class handles jwt functionallity.
    """
    def create_token(user: User) -> str:
        payload = {
            "userId": user.id,
        }
        wt_token = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")