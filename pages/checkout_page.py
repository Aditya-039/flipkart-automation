# pages/checkout_page.py

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    CONTINUE_BTN    = (
        By.XPATH,
        "//button[contains(translate(normalize-space(.),"
        "'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'continue')]"
    )
    ACCEPT_CONTINUE = (
        By.XPATH,
        "//button[contains(., 'Accept & Continue') or contains(., 'Agree & Continue')]"
    )
    DELIVER_HERE    = (
        By.XPATH,
        "//button[contains(normalize-space(.),'Deliver Here')]"
    )
    CARD_OPTION     = (
        By.XPATH,
        "//label[contains(translate(normalize-space(.),"
        "'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'credit')"
        " and contains(translate(normalize-space(.),"
        "'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'card')]"
    )
    PAY_BTN         = (
        By.XPATH,
        "//button[contains(translate(normalize-space(.),"
        "'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'pay')]"
    )
    OTP_INPUT       = (By.NAME, "otp")

    def __init__(self, driver):
        self.driver = driver

    def proceed_to_payment(self):
        """Click CONTINUE and dismiss the open-box popup."""
        btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CONTINUE_BTN)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
        btn.click()
        try:
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.ACCEPT_CONTINUE)
            ).click()
        except TimeoutException:
            pass

    def complete_payment(
        self,
        card_no: str,
        exp: str,
        cvv: str,
        pincode: str,
        country: str,
        city: str,
        state: str,
        address: str
    ):
        """
        1) (Optional) Deliver Here
        2) Click Credit/Debit Card
        3) Fill cardNumber, month/year, CVV
        4) Fill billing fields
        5) Click Pay
        """
        # 1) Deliver Here
        try:
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.DELIVER_HERE)
            ).click()
        except TimeoutException:
            pass

        # 2) Reveal the card form
        card_opt = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.CARD_OPTION)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", card_opt)
        card_opt.click()

        # 3a) Card Number
        card_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "cardNumber"))
        )
        card_input.send_keys(card_no)

        # 3b) Expiry
        month_str, year_str = exp.split("/")
        Select(self.driver.find_element(By.NAME, "month")).select_by_value(month_str)
        Select(self.driver.find_element(By.NAME, "year")).select_by_value(year_str)

        # 3c) CVV
        cvv_input = self.driver.find_element(By.NAME, "cvv")
        cvv_input.send_keys(cvv)

        # 4) Billing fields
        #    Zip/Pincode
        pin = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "billing_pincode"))
        )
        pin.send_keys(pincode)

        #    Country select
        Select(self.driver.find_element(By.NAME, "billing_country"))\
            .select_by_visible_text(country)

        #    City
        self.driver.find_element(By.NAME, "billing_city").send_keys(city)

        #    State
        self.driver.find_element(By.NAME, "billing_state").send_keys(state)

        #    Address textarea
        self.driver.find_element(By.NAME, "billing_address").send_keys(address)

        # 5) Click Pay
        pay_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.PAY_BTN)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", pay_btn)
        pay_btn.click()

    def is_on_otp_page(self) -> bool:
        """Return True once the OTP input appears on screen."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.OTP_INPUT)
            )
            return True
        except TimeoutException:
            return False
