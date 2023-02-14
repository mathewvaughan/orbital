from fastapi.testclient import TestClient

from .main import get_app
from .data import data

client = TestClient(get_app(
    data
))

def test_detail_endpoint():
    response = client.get("/api/titles/1")
    assert response.status_code == 200
    assert response.json() == data[1]

def test_detail_endpoint_not_found():
    response = client.get("/api/titles/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}
