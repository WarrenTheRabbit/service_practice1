import pytest
from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)

def test_that_the_root_path_responds():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "This is the root of service1."}
    
