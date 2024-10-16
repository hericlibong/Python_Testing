import pytest
from flask import Flask
from server import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Sad path: Python_Testing/tests/functional/test_unknown_email_functional.py
def test_unknown_email(client):
    # Suivre la redirection pour voir si le message apparaît sur la page d'index
    response = client.post('/showSummary', data={'email': 'unknown@example.com'}, follow_redirects=True)
    
    # Afficher le contenu pour confirmer la redirection et le message
    print(response.data.decode())  
    
    # Vérifier que le message d'erreur est bien présent dans la page d'accueil
    assert b"The entered email is unknown. Please try again with a valid email." in response.data


# Happy path: Python_Testing/tests/functional/test_unknown_email_functional.py
def test_known_email(client):
    response = client.post('/showSummary', data={'email': 'john@simplylift.co'}, follow_redirects=True)
    assert b"Welcome" in response.data
    assert b"Points available" in response.data


