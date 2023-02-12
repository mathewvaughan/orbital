from fastapi.testclient import TestClient

from .main import get_app
from .data import data

client = TestClient(get_app(
    data
))

def test_read_main():
    response = client.get("/api/titles")
    assert response.status_code == 200
    assert response.json() == data