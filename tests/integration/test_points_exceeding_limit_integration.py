import pytest
from flask import Flask
from server import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_integration_points_exceeding_limit(client):
    response = client.post('/purchasePlaces', data={
        'competition': 'Spring Festival', 
        'club': 'Simply Lift', 
        'places': '50'  # Test de bout en bout
    })
    assert b"You don&#39;t have enough points to complete this booking." in response.data
