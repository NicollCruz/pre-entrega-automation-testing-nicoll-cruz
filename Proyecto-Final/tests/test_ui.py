import pytest
import json
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.logger import get_logger
from pages.checkout_page import CheckoutPage

logger = get_logger("UI_Tests")

def test_login_exitoso(driver):
    """Caso 1: Verificar el login con credenciales válidas"""
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    
    logger.info("Ejecutando Caso 1: Login Exitoso.")
    login_page.open()
    login_page.login_user("standard_user", "secret_sauce")
    
    assert "inventory.html" in driver.current_url
    assert inventory_page.get_title_text() == "Products"
    logger.info("Caso 1 PASSED: Redirección e interfaz validadas.")

def test_login_usuario_bloqueado(driver):
    """Caso 2 (Negativo): Intentar ingresar con un usuario bloqueado"""
    login_page = LoginPage(driver)
    
    logger.info("Ejecutando Caso 2: Login Negativo (Usuario Bloqueado)")
    login_page.open()
    login_page.login_user("locked_out_user", "secret_sauce")
    
    # Validamos que muestre el error
    assert "inventory.html" not in driver.current_url
    assert login_page.get_error_text() != ""
    logger.warning("Caso 2 PASSED: El sistema bloqueó el acceso correctamente.")

def test_login_credenciales_invalidas(driver):
    """Caso 3 (Negativo): Intentar ingresar con un usuario inválido."""
    login_page = LoginPage(driver)
    
    logger.info("Ejecutando Caso 3: Login Negativo (Datos Falsos)")
    login_page.open()
    login_page.login_user("usuario_falso_utn", "clave_cualquiera")
    
    assert "inventory.html" not in driver.current_url
    assert login_page.get_error_text() != ""
    logger.warning("Caso 3 PASSED: Alerta de seguridad disparada correctamente.")


def test_busqueda_y_filtros_catalogo(driver):
    """Caso 4: Validar la organización y búsqueda mediante filtros"""
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    
    logger.info("Ejecutando Caso 4: Filtros de Catálogo.")
    login_page.open()
    login_page.login_user("standard_user", "secret_sauce")
    
    # Filtro de ordenamiento por precio
    inventory_page.filter_by_price_low_to_high()
    lowest_price = inventory_page.get_first_product_price()
    
    # Primer elemento más económico ($7.99)
    assert lowest_price == "$7.99"
    logger.info("Caso 4 PASSED: Filtro de menor a mayor aplicado correctamente.")

def test_flujo_checkout_completo(driver):
    """Caso 5: Validar compra completa desde el carrito hasta la confirmación de pago"""
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    checkout_page = CheckoutPage(driver)
    
    logger.info("Ejecutando Caso 5: Flujo completo de Compra.")
    
  
    login_page.open()
    login_page.login_user("standard_user", "secret_sauce")     
    inventory_page.add_backpack_to_cart()                    
    assert inventory_page.get_cart_badge_text() == "1"
    
    inventory_page.go_to_cart()                               # Navegación al Carrito
    checkout_page.start_checkout()                            # Inicio de Checkout
    
    checkout_page.fill_shipping_data("Nicoll", "Cruz", "1828") # Formulario de envío
    checkout_page.complete_order()                            # Confirmación de Pago
    
    assert checkout_page.get_confirmation_message() == "Thank you for your order!"
    logger.info("Caso 5 PASSED: Compra finalizada de punta a punta con éxito.")