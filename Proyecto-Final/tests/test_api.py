import pytest
import requests
from utils.logger import get_logger

logger = get_logger("API_Tests")

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_users():
    logger.info("Enviando petición GET a /users")
    response = requests.get(f"{BASE_URL}/users/1")
    
    assert response.status_code == 200
    json_data = response.json()
    assert "name" in json_data
    logger.info("API GET validada con código 200 y estructura JSON correcta.")

def test_create_user():
    payload = {"title": "Nicoll QA", "body": "Automation Test", "userId": 1}
    logger.info("Enviando petición POST a /posts para creación de recurso.")
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    
    assert response.status_code == 201
    json_data = response.json()
    assert json_data["title"] == payload["title"]
    assert "id" in json_data
    logger.info(f"API POST exitosa. Recurso creado con ID: {json_data['id']}.")

def test_delete_user():
    logger.info("Enviando petición DELETE a /posts/1")
    response = requests.delete(f"{BASE_URL}/posts/1")
    
    assert response.status_code == 200
    logger.info("API DELETE verificada con código de estado 200.")