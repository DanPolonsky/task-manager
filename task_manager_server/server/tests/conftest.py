import pytest
import os
import logging

from flask.testing import FlaskClient
from server import app

@pytest.fixture(scope="session")
def client() -> FlaskClient:
    flask_client = app.test_client()
    return flask_client


class shared_values:
    headers = None