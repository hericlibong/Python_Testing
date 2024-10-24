import pytest
from flask import Flask
from server import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Simulate the case where the places requested exceed the limit of available places
def test_not_enough_places(client):
    response = client.post('/purchasePlaces', data={
        'competition': 'Titan Challenge', 
        'club': 'Power Surge', 
        'places': '11'  # End-to-end test
    })
    assert b"Not enough places available for this competition" in response.data

