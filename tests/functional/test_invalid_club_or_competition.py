import pytest
from flask import Flask
from server import app



@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Simulate case where club or competition is not found
def test_invalid_club_or_competition(client):
    # Simuler une compétition ou un club inexistant
    response = client.get('/book/NonExistentCompetition/NonExistentClub', follow_redirects=True)
    assert b"Club or competition not found." in response.data



