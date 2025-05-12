from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    PLACE_ORDER = (By.XPATH, "//button[contains(., 'Place Order')]")

    def __init__(self, driver):
        self.driver = driver

    def place_order(self):
        # wait for “Place Order” and click it
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.PLACE_ORDER)
        ).click()
