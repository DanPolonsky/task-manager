import pytest
import logging
from flask.testing import FlaskClient
from server.tests.properties import user, project
from server.tests.utils import print_response, response_is_valid
from server.properties import request_properties, response_properties
from server.tests.conftest import shared_values

"""
    This module contains positive user api functions tests.
"""



def test_user_creation(client: FlaskClient):
    logging.info(f"Creating user: {user}")
    response = client.post("/auth/register", json=user)
    print_response(response)
    assert response_is_valid(response)
    
    shared_values.headers = {
        request_properties.header_keys.authrorization: f"{request_properties.header_values.bearer} {response.json[response_properties.payload_keys.data][response_properties.payload_keys.token]}"
    }


def test_project_creation(client: FlaskClient):
    logging.info(f"Creating project: {project}")
    response = client.post("/user/projects", headers=shared_values.headers, json=project)
    print_response(response)
    assert response_is_valid(response)
    shared_values.project_id = response.json[response_properties.payload_keys.data][response_properties.payload_keys.project_id]


def test_project_deletion(client: FlaskClient):
    logging.info(f"Creating project: {project}")
    response = client.delete("/user/projects", headers=shared_values.headers, json={
        request_properties.payload_keys.project_id: shared_values.project_id
    })
    print_response(response)
    assert response_is_valid(response)
