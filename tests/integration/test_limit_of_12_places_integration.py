import pytest
from flask import Flask
from server import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_limit_of_12_places(client):
    response = client.post('/purchasePlaces', data={
        'competition': 'Alpha Power Meet', 
        'club': 'Iron Paradise', 
        'places': '13'  # Test pour vérifier que plus de 12 places ne peuvent être réservées
    })
    assert b"You cannot book more than 12 places per competition." in response.data
