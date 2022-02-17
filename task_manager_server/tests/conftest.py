import pytest
import os
import logging

from flask.testing import FlaskClient

@pytest.fixture(scope="session")
def client() -> FlaskClient:
    logging.info("Setting server config")
    os.environ["CONFIG"] = "config.Testing"
    
    from server import app
    flask_client = app.test_client()

    return flask_client

