import pytest
from flask import Flask
from server import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# simulate empty form submission for competition and club
def test_error_occurred(client):
    response = client.post('/purchasePlaces', data={
        'competition': '', 
        'club': '', 
        'places': '5'
    }, follow_redirects=True)
    assert b"An error occurred. Please try again." in response.data
    