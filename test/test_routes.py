import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app_main import app
import pytest

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"FairDeal Bot is Live!" in response.data

def test_webhook_route(client):
    payload = {"message": "hello"}
    response = client.post('/webhook', json=payload)
    assert response.status_code == 200
