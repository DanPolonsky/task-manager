from server.route_handlers.response import Response


def login_handler(request):
    if request.method == 'POST':
        data = request.json

        if "email" not in data or "password" not in data:
            return Response(success=False, data="missing email or password keys.")
        
        if not isinstance(data["email"], str) or not isinstance(data["password"], str):
            return Response(success=False, data="email or password type are not string.")

        
        return Response(success=True)



