from fastapi.testclient import TestClient

from .main import get_app

client = TestClient(get_app(
    [
        {
            "id": "0",
            "title_number": "MYBKZ10625",
            "title_class": "Freehold",
            "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean convallis lectus velit, ac mollis lorem fringilla ac. In consequat molestie dui, et pellentesque nisl convallis at. Curabitur dictum lacinia justo, pulvinar pharetra purus ru"
        },
    ]
))

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}