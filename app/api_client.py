import requests

# esto simula una api externa. url falsa para pruebas con mocks.
def fetch_data():
    response = requests.get("https://api.prueba.com/datos")
    response.raise_for_status()
    return response.json()
