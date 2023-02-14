from fastapi.testclient import TestClient

from .main import get_app
from .data import data

client = TestClient(get_app(
    data
))

def test_list_endpoint_returns_paginated_response():
    response = client.get("/api/titles")
    assert response.status_code == 200
    assert response.json()["page"] == 1
    assert response.json()["size"] == 50
    assert response.json()["total"] == len(data)
    assert response.json()["items"] == data[:10]