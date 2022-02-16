import pytest

""" 
    Module containing fixture properties for tests use.
"""

@pytest.fixture(scope="session")
def user():
    return {
        "username": "user-name",
        "email": "email@gmail.com",
        "password": "some-password"
    }

@pytest.fixture(scope="session")
def project():
    return {
        "name": "project-name",
        "description": "This is a project's description",
    }


