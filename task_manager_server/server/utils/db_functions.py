from server import db
from server.models import User
import hashlib

"""
    This module contains a list of functions for communication with the database.
"""


### Utils functions

def hash_password(password: str):
    m = hashlib.sha256()
    m.update(password.encode())
    return m.hexdigest()


### User functions

def check_if_username_exists(username: str) -> bool:
    """ Function checks if user with the provided username exists in database.

    Args:
        username (str): A username to check if exists.

    Returns:
        [bool]: Returns whether username exists in database.
    """
    if User.query.filter_by(username=username).first():
        return True
    else:
        return False
    

def check_if_email_exists(email: str) -> bool:
    """ Function checks if user with the provided email exists in database.

    Args:
        email (str): A email to check if exists.

    Returns:
        [bool]: Returns whether email exists in database.
    """
    if User.query.filter_by(email=email).first():
        return True
    else:
        return False


def get_user_by_email(email: str) -> User:
    """ Function gets a user from the database using email.

    Args:
        email (str): The user's email.

    Returns:
        [User]: The user object.
    """
    return User.query.filter_by(email=email).first()


def create_user(email: str, username: str, password: str) -> None:
    """ Function creates a new user in database with the provided data.

    Args:
        email (str): The user's email.
        username (str): The user's username.
        password (str): The user's plane password.
    """
    
    hashed_password = hash_password(password)
    
    db.session.add(User(
        email=email,
        username=username,
        password=hashed_password
    ))

    db.session.commit()