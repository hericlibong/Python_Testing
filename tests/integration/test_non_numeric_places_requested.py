import pytest
from server import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


# Simulate case with non-numeric places requested
def test_non_numeric_places_requested(client):
    response = client.post('/purchasePlaces', data={
        'competition': 'Titan Challenge',
        'club': 'Power Surge',
        'places': 'abc'  # End-to-end test
    }, follow_redirects=True)
    assert b"Invalid number of places. Please enter a valid positif number in the field." in response.data
