from fastapi.testclient import TestClient

from .main import get_app
from .data import data

client = TestClient(get_app(
    data
))

def test_list_data_from_endpoint():
    response = client.get("/api/titles")
    assert response.status_code == 200
    assert response.json() == data

def test_detail_endpoint():
    response = client.get("/api/titles/1")
    assert response.status_code == 200
    assert response.json() == data[1]