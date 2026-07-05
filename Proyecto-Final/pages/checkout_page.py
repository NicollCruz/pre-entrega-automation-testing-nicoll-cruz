from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    CHECKOUT_BUTTON = (By.ID, "checkout")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def start_checkout(self):
        self.click(self.CHECKOUT_BUTTON)

    def fill_shipping_data(self, first_name, last_name, zip_code):
        self.write(self.FIRST_NAME, first_name)
        self.write(self.LAST_NAME, last_name)
        self.write(self.POSTAL_CODE, zip_code)
        self.click(self.CONTINUE_BUTTON)

    def complete_order(self):
        self.click(self.FINISH_BUTTON)

    def get_confirmation_message(self):
        return self.get_text(self.COMPLETE_HEADER)