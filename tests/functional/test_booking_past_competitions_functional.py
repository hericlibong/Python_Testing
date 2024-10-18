import pytest
from flask import Flask
from server import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Test fonctionnel : tenter de réserver une compétition passée
def test_attempt_booking_past_competition(client):
    response = client.post('/purchasePlaces', data={
        'competition': 'Spring Festival',
        'club': 'Simply Lift',
        'places': '5'
    }, follow_redirects=True)

    # Vérifier que le message d'erreur concernant la compétition passée est présent
    assert b"This competition has already taken place. No reservations allowed." in response.data


# Test fonctionnel : tenter de réserver une compétition future
def test_success_booking_future_competition(client):
    response = client.post('/purchasePlaces', data={
        'competition': 'Summer Bash',
        'club': 'Simply Lift',
        'places': '5'
    }, follow_redirects=True)

    # Vérifier que la réservation a été effectuée avec succès
    assert b"Successfully booked" in response.data