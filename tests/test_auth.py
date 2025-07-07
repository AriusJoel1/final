import pytest

# fixture de usuario basico
@pytest.fixture
def user_fixture():
    return {
        "username": "testuser",
        "email": "test@example.com",
        "token": "abc123"
    }

# fixture que depende del usuario
@pytest.fixture
def authenticated_client_fixture(user_fixture):
    class FakeClient:
        def __init__(self, token):
            self.token = token

        def is_authenticated(self):
            return bool(self.token)

    return FakeClient(token=user_fixture["token"])


# prueba fallara por falta de token
@pytest.mark.xfail(reason="No hay token de autenticación")
def test_access_without_token():
    client = type("FakeClient", (), {"token": None, "is_authenticated": lambda self: False})()
    assert client.is_authenticated()


# prueba no implementada
@pytest.mark.skip(reason="todavia no esta implementada")
def test_feature_not_implemented():
    assert False  
