import pytest
from flask import Flask
from server import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_points_update_after_booking(client):
    # Supposons que le club Simply Lift ait 13 points et qu'il réserve 5
    response = client.post('/purchasePlaces', data={
        'competition': 'Winter Games', 
        'club': 'Simply Lift', 
        'places': '5'
    }, follow_redirects=True)

    # Vérifier que la mise à jour de points est correcte après la réservation
    assert b"Points available: 8" in response.data
    assert b"Successfully booked 5 places for Winter Games" in response.data


    