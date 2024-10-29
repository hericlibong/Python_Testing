import pytest
from server import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


# Tester la déconnexion
def test_logout(client):
    with client.session_transaction() as sess:
        sess['user'] = 'testUser'
    response = client.get('/logout')
    assert response.status_code == 302  # Redirection
    with client.session_transaction() as sess:
        assert 'user' not in sess  # Session devrait être vide
