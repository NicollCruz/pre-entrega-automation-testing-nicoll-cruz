import pytest
import requests
from utils.logger import get_logger

logger = get_logger("API_Tests")
BASE_URL = "https://reqres.in/api"

def test_get_users():
    logger.info("Enviando petición GET a /users")
    response = requests.get(f"{BASE_URL}/users?page=2")
    
    assert response.status_code == 200
    json_data = response.json()
    assert "data" in json_data
    assert len(json_data["data"]) > 0
    logger.info("API GET validada con código 200 y estructura JSON correcta.")

def test_create_user():
    payload = {"name": "Nicoll", "job": "Automation QA"}
    logger.info("Enviando petición POST a /users para creación de recurso.")
    response = requests.post(f"{BASE_URL}/users", json=payload)
    
    assert response.status_code == 201
    json_data = response.json()
    assert json_data["name"] == payload["name"]
    assert "id" in json_data
    logger.info(f"API POST exitosa. Recurso creado con ID: {json_data['id']}.")

def test_delete_user():
    logger.info("Enviando petición DELETE a /users/2")
    response = requests.delete(f"{BASE_URL}/users/2")
    
    assert response.status_code == 204
    logger.info("API DELETE verificada con código de estado 204 (No Content).")