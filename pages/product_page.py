# pages/product_page.py

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    # Interstitials
    TRY_NOW     = (By.XPATH, "//button[contains(., 'Try now')]")
    RETRY_MSG   = (By.XPATH, "//div[contains(., 'retry in')]")
    RETRY_BTN   = (By.XPATH, "//button[contains(., 'Retry')]")

    # Primary CTAs
    ADD_TO_CART = (
        By.XPATH,
        "//button[contains(translate(normalize-space(.),"
        "'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),"
        "'add to cart')]"
    )
    GO_TO_CART  = (
        By.XPATH,
        "//button[contains(translate(normalize-space(.),"
        "'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),"
        "'go to cart')]"
    )

    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):
        # 0) Handle site‐maintenance “Try now”
        try:
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.TRY_NOW)
            ).click()
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.ADD_TO_CART)
            )
        except TimeoutException:
            pass

        # 1) Handle bot‐check “retry in X seconds”
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.RETRY_MSG)
            )
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(self.RETRY_BTN)
            ).click()
        except TimeoutException:
            pass

        # 2) If it’s already in cart, click “Go to cart” and return
        try:
            go_btn = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.GO_TO_CART)
            )
            go_btn.click()
            return
        except TimeoutException:
            pass

        # 3) Otherwise click “Add to Cart”
        add_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.ADD_TO_CART)
        )
        add_btn.click()
