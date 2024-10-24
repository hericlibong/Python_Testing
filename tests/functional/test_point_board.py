import pytest
from flask import Flask
from server import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Tester l'affichage des points dans le tableau de bord
def test_point_board(client):
    response = client.get('/pointBoard')
    assert response.status_code == 200
    assert b"Points Available" in response.data
    assert b"Club Name" in response.data