"""Pruebas unitarias para el pipeline."""

from unittest.mock import Mock
from unittest.mock import patch

import pytest
import requests

from pipeline import obtener_personajes


@patch("pipeline.requests.get")
def test_obtener_personajes_devuelve_registros(mock_get):
    mock_response = Mock()

    mock_response.json.return_value = {
        "info": {"next": None},
        "results": [
            {
                "id": 1,
                "name": "Rick Sanchez",
                "status": "Alive",
                "species": "Human",
                "gender": "Male",
                "origin": {"name": "Earth"},
                "location": {"name": "Citadel of Ricks"},
            }
        ],
    }

    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    datos = list(obtener_personajes())

    assert len(datos) == 1


@patch("pipeline.requests.get")
def test_estructura_correcta(mock_get):
    mock_response = Mock()

    mock_response.json.return_value = {
        "info": {"next": None},
        "results": [
            {
                "id": 1,
                "name": "Rick Sanchez",
                "status": "Alive",
                "species": "Human",
                "gender": "Male",
                "origin": {"name": "Earth"},
                "location": {"name": "Citadel of Ricks"},
            }
        ],
    }

    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    registro = list(obtener_personajes())[0]

    assert "id" in registro
    assert "name" in registro
    assert "species" in registro
    assert "status" in registro


@patch("pipeline.requests.get")
def test_respuesta_vacia(mock_get):
    mock_response = Mock()

    mock_response.json.return_value = {
        "info": {"next": None},
        "results": [],
    }

    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    datos = list(obtener_personajes())

    assert datos == []


@patch("pipeline.requests.get")
def test_error_conexion(mock_get):
    mock_get.side_effect = requests.ConnectionError()

    with pytest.raises(requests.ConnectionError):
        list(obtener_personajes())


@patch("pipeline.requests.get")
def test_nombre_es_string(mock_get):
    mock_response = Mock()

    mock_response.json.return_value = {
        "info": {"next": None},
        "results": [
            {
                "id": 1,
                "name": "Rick Sanchez",
                "status": "Alive",
                "species": "Human",
                "gender": "Male",
                "origin": {"name": "Earth"},
                "location": {"name": "Citadel of Ricks"},
            }
        ],
    }

    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    registro = list(obtener_personajes())[0]

    assert isinstance(registro["name"], str)