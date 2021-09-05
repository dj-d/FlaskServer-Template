from src import create_app


def test_config():
    assert not create_app().testing


def test_hello(client):
    response = client.get('/health-check')
    assert response.data == b'Server is running...'
