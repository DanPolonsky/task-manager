import pytest
import logging

from tests.properties import user, project
from flask.testing import FlaskClient

from tests.utils import print_response, response_is_valid

"""
    This module contains positive user api functions tests.
"""



def test_user_creation(client: FlaskClient):
    logging.info(f"Creating user: {user}")
    response = client.post("/auth/register", json=user)
    print_response(response)
    assert not response_is_valid(response)

