import pytest
import json
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.logger import get_logger

logger = get_logger("UI_Tests")

def load_user_data():
    with open("data/users.json") as f:
        return json.load(f)

@pytest.mark.parametrize("user", load_user_data())
def test_login_scenarios(driver, user):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    
    logger.info(f"Iniciando test de login para usuario: {user['username']}")
    login_page.open()
    login_page.login_user(user['username'], user['password'])
    
    if user['expected_type'] == "valid":
        assert "inventory.html" in driver.current_url
        assert inventory_page.get_title_text() == "Products"
        logger.info("Login exitoso verificado correctamente.")
    else:
        assert login_page.get_error_text() != ""
        logger.warning("Escenario negativo validado con captura de error en UI.")

def test_catalog_and_cart_flow(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    
    logger.info("Ejecutando flujo completo de catálogo y adición al carrito.")
    login_page.open()
    login_page.login_user("standard_user", "secret_sauce")
    
    # Validar catálogo
    assert inventory_page.get_products_count() > 0
    
    # Interacción de Carrito
    inventory_page.add_backpack_to_cart()
    assert inventory_page.get_cart_badge_text() == "1"
    logger.info("Flujo de catálogo e incremento de productos en carrito exitoso.")