import pytest
import logging

from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_that_the_root_path_responds():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "This is the root of service1."}
    

def test_that_requests_are_logged(caplog):
    with caplog.at_level(logging.INFO, logger="service1"):
        client.get("/")
        assert str({'url': '/', 'method': 'GET'}) in caplog.text
        
def test_that_routes_are_logged_automatically(caplog):
    with caplog.at_level(logging.INFO, logger="service1"):
        client.get("/nonexistent_route")
        assert "'url': '/nonexistent_route'" in caplog.text