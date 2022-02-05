from server.route_handlers.response import Response
import re


def signup_handler(request):
    if request.method == 'POST':
        data = request.json

        if "email" not in data or "username" not in data or "password" not in data:
            return Response(success=False, data="missing email or password keys.")
        
        if not isinstance(data["email"], str) or not isinstance(data["password"], str) or not isinstance(data["username"], str):
            return Response(success=False, data="email, username or password types are not string.")
        
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.fullmatch(email_regex, data["email"]):
            return Response(success=False, data="email is not in a correct format.")
        
        if len(data["password"]) < 6:
            return Response(success=False, data="password length must be above 6 characters.")
        
        

        return Response(success=True)