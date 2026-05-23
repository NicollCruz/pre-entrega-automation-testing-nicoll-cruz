import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService

from utils.functions import login, get_first_product_data
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_full_flow(driver):
    #Navegar y Login
    driver.get("https://www.saucedemo.com")
    login(driver, "standard_user", "secret_sauce")
    
    #Login
    assert "inventory.html" in driver.current_url
    assert driver.find_element(By.CLASS_NAME, "title").text == "Products"

    #Catálogo
    nombre, precio = get_first_product_data(driver)
    print(f"Producto: {nombre} - Precio: {precio}")
    assert len(driver.find_elements(By.CLASS_NAME, "inventory_item")) > 0

    #Carrito
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    
    badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert badge == "1"

    # Navegar al carrito y verificar producto
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    item_in_cart = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert item_in_cart == nombre