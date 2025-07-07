import pytest
from unittest.mock import create_autospec
import requests
import app.api_client as api_client


def test_fetch_data_success(mocker):
    mock_get = mocker.patch("requests.get", autospec=True)
    
    # simula respuesta exitosa
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": "ok"}
    mock_response.raise_for_status = mocker.Mock()
    mock_get.return_value = mock_response

    data = api_client.fetch_data()

    assert data["result"] == "ok"
    mock_get.assert_called_with("https://api.prueba.com/datos")


def test_fetch_data_multiple_calls(mocker):
    mock_get = mocker.patch("requests.get", autospec=True)

    # simula multiples respuestas
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"valor": "ok"}
    mock_response.raise_for_status = mocker.Mock()
    mock_get.return_value = mock_response

    for _ in range(3):
        api_client.fetch_data()

    assert len(mock_get.call_args_list) == 3


def test_fetch_data_network_error(mocker):
    mock_get = mocker.patch("requests.get", autospec=True)
    mock_get.side_effect = requests.exceptions.ConnectionError("Fallo de red")

    with pytest.raises(requests.exceptions.ConnectionError):
        api_client.fetch_data()
