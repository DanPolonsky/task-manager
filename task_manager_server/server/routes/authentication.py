from flask import request
from server.routes.response import Response

from server import app, db
from server.models import User

@app.route('/login', methods = ['POST'])
def login():
    if request.method == 'POST':
        data = request.json

        if "email" not in data or "password" not in data:
            return Response(success=False, data="missing email or password keys.")
        
        if not isinstance(data["email"], str) or not isinstance(data["password"], str):
            return Response(success=False, data="email or password type are not string.")

        
        return Response(success=True)



@app.route('/signup', methods = ['POST'])
def signup():
    if request.method == 'POST':
        data = request.json

        if "email" not in data or "username" not in data or "password" not in data:
            return Response(success=False, data="missing email or password keys.")
        
        if not isinstance(data["email"], str) or not isinstance(data["password"], str) or not isinstance(data["username"], str):
            return Response(success=False, data="email, username or password types are not string.")
        
        
        return Response(success=True)