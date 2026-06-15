# test_app.py
import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home_returns_200(client):
    response = client.get("/")
    assert response.status_code == 200

def test_todos_returns_list(client):
    response = client.get("/todos")
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_invalid_todo_returns_404(client):
    response = client.get("/todos/999")
    assert response.status_code == 404