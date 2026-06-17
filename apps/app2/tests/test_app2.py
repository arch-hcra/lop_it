from app2 import app
import pytest

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello from my App2!11!!" in response.data
