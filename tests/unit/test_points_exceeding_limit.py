import pytest
from flask import Flask
from server import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_points_exceeding_limit(client):
    response = client.post('/purchasePlaces', data={
        'competition': 'Spring Festival', 
        'club': 'Simply Lift', 
        'places': '50'  # Supposons que le club n'ait pas assez de points
    })
    assert b"You don&#39;t have enough points to complete this booking." in response.data


