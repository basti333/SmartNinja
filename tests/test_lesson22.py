import pytest
import os
from Lesson22.main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    os.environ['TESTING'] = '1'
    client = app.test_client()
    yield client

def test_index_not_logged_in(client):
    response = client.get('/')
    assert b'Enter your name' in response.data

def test_index_logged_in(client):
    client.post('/login', data={"user-name": "Test User", "user-email": "test@user.com", "user-password": "password123"}, follow_redirects=True)
    response = client.get('/')
    assert b'Enter your guess' in response.data

