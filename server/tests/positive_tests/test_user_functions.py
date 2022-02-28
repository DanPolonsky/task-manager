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
    logging.info(f"Checking if project got created: {project}")
    response = client.get("/user/projects", headers=shared_values.headers)
    print_response(response)
    for project_info in response.json[response_properties.payload_keys.data][response_properties.payload_keys.projects]:
        if project_info["id"] == shared_values.project_id:
            assert True
            return
    
    assert False


def test_project_deletion(client: FlaskClient):
    logging.info(f"Deleting project: {project}")
    response = client.delete("/user/projects", headers=shared_values.headers, json={
        request_properties.payload_keys.project_id: shared_values.project_id
    })
    print_response(response)
    assert response_is_valid(response)
    logging.info(f"Checking if project got deleted: {project}")
    response = client.get("/user/projects", headers=shared_values.headers)
    print_response(response)
    for project_info in response.json[response_properties.payload_keys.data][response_properties.payload_keys.projects]:
        if project_info["id"] == shared_values.project_id:
            assert False
    
    assert True


def test_user_deletion(client: FlaskClient):
    logging.info(f"Deleting user: {user}")
    response = client.delete("/users", headers=shared_values.headers)
    
    print_response(response)
    assert response_is_valid(response)
    
def test_false():
    assert False

