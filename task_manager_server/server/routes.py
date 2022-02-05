from flask import request
from server import app
from server.route_handlers.authentication.login import login_handler
from server.route_handlers.authentication.signup import signup_handler

@app.route('/login', methods = ['POST'])
def login():
    return login_handler(request)

@app.route('/signup', methods = ['POST'])
def signup():
    return signup_handler(request)