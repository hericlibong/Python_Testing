import pytest
from flask import Flask
from server import app
from datetime import datetime

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


# Test pour les compétitions passées
def test_booking_past_competitions(client):
    response = client.get('/book/Spring-Festival/Simply-Lift', follow_redirects=True)

    # Vérifier que la compétition est passée et que le message d'erreur apparaît
    assert b"This competition has already taken place. No reservations allowed." in response.data


# Test pour les compétitions en cours ou futures
def  test_booking_future_competition(client):
    response = client.get('/book/Summer-Bash/Simply-Lift', follow_redirects=True)

    # Vérifier que la page de réservation s'affiche correctement pour la competition
    assert b"How many places?" in response.data