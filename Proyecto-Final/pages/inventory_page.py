from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    ADD_BACKPACK_BTN = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    PRODUCTS = (By.CLASS_NAME, "inventory_item")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    FIRST_PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def get_title_text(self):
        return self.get_text(self.TITLE)

    def get_products_count(self):
        self.find_element(self.PRODUCTS)
        return len(self.driver.find_elements(*self.PRODUCTS))

    def add_backpack_to_cart(self):
        self.click(self.ADD_BACKPACK_BTN)

    def get_cart_badge_text(self):
        return self.get_text(self.CART_BADGE)
    
    def filter_by_price_low_to_high(self):
        # Selecciona la opción de ordenar por precio menor a mayor
        dropdown = self.find_element(self.SORT_DROPDOWN)
        dropdown.send_keys("Price (low to high)")

    def get_first_product_price(self):
        return self.get_text(self.FIRST_PRODUCT_PRICE)

    def go_to_cart(self):
        self.click(self.CART_ICON)