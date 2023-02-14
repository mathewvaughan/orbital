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

def test_list_endpoint_returns_paginated_response_with_custom_page_size():
    response = client.get("/api/titles?size=5")
    assert response.status_code == 200
    assert response.json()["page"] == 1
    assert response.json()["size"] == 5
    assert response.json()["total"] == len(data)
    assert response.json()["items"] == data[:5]

def test_list_endpoint_returns_paginated_response_with_custom_page():
    response = client.get("/api/titles?page=2&size=5")
    assert response.status_code == 200
    assert response.json()["page"] == 2
    assert response.json()["size"] == 5
    assert response.json()["total"] == len(data)
    assert response.json()["items"] == data[5:9]

def test_list_endpoint_order_by_id_descending():
    response = client.get("/api/titles?_sort=id&_order=desc")
    assert response.status_code == 200
    assert response.json()["items"] == sorted(data, key=lambda x: x["id"], reverse=True)[:10]

def test_list_endpoint_order_by_id_ascending():
    response = client.get("/api/titles?_sort=id&_order=asc")
    assert response.status_code == 200
    assert response.json()["items"] == sorted(data, key=lambda x: x["id"])[:10]

def test_list_endpoint_order_by_title_number_descending():
    response = client.get("/api/titles?_sort=title_number&_order=desc")
    assert response.status_code == 200
    assert response.json()["items"] == sorted(data, key=lambda x: x["title_number"], reverse=True)[:10]