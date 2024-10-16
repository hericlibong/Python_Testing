import pytest
from flask import Flask
from server import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Sad path: Python_Testing/tests/unit/test_unknown_email.py
def test_unknown_email(client):
    # Suivre la redirection pour voir si le message apparaît sur la page d'index
    response = client.post('/showSummary', data={'email': 'unknown@example.com'}, follow_redirects=True)
    
    # Afficher le contenu pour confirmer la redirection et le message
    print(response.data.decode())  # Décommenter pour voir le contenu lors du test
    
    # Vérifier que le message d'erreur est bien présent dans la page d'accueil
    assert b"The entered email is unknown. Please try again with a valid email." in response.data


# Happy path: Python_Testing/tests/unit/test_unknown_email.py
def test_known_email(client):
    response = client.post('/showSummary', data={'email': 'john@simplylift.co'}, follow_redirects=True)
    
    # Vérifie si la page de bienvenue contient le nom du club ou tout autre indicatif de succès
    assert b"Welcome" in response.data
    assert b"Points available" in response.data

