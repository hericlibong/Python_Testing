import pytest
from server import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Simulate a case where the number of places requested is negative
def test_negative_places_requested(client):
    response = client.post('/purchasePlaces', data={
        'competition': 'Titan Challenge', 
        'club': 'Power Surge', 
        'places': '-5'  # End-to-end test
    }, follow_redirects=True)
    # Vérifier que le message pour une valeur positive est affiché
    assert b"Please enter a positive number of places." in response.data