from fastapi.testclient import TestClient

from .main import get_app

data = [
        {
            "id": "0",
            "title_number": "MYBKZ10625",
            "title_class": "Freehold",
            "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean convallis lectus velit, ac mollis lorem fringilla ac. In consequat molestie dui, et pellentesque nisl convallis at. Curabitur dictum lacinia justo, pulvinar pharetra purus ru"
        },
    ]

client = TestClient(get_app(
    data
))

def test_read_main():
    response = client.get("/api/titles")
    assert response.status_code == 200
    assert response.json() == data