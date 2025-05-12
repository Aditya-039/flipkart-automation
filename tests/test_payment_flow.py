# tests/test_payment_flow.py

import pytest
from pages.product_page   import ProductPage
from pages.cart_page      import CartPage
from pages.checkout_page  import CheckoutPage

PRODUCT_URL = (
    "https://www.flipkart.com/boult-bassbox-q5-upto-18h-battery-5w-bass-output-"
    "compact-size-multiple-modes-5-4v-5-w-bluetooth-speaker/p/itmfcfbd1d853907"
)
CARD_NO     = "4111111111111111"
EXPIRY      = "12/25"
CVV         = "123"

# billing details to satisfy Flipkart’s form
PIN_CODE    = "743125"
COUNTRY     = "India"
CITY        = "Bhatpara"
STATE       = "West Bengal"
ADDRESS     = (
    "Kamla niwas 26 guptar bagan holding no 19/b jagtdal, "
    "24 pgs north jagatdal, Bhatpara"
)

def test_reach_payment_otp(driver):
    # 1) Open the product page
    driver.get(PRODUCT_URL)

    # 2) Add to cart & place order
    ProductPage(driver).add_to_cart()
    CartPage(driver).place_order()

    # 3) Skip summary + popup
    checkout = CheckoutPage(driver)
    checkout.proceed_to_payment()

    # 4) Fill card + billing details, then Pay
    checkout.complete_payment(
        CARD_NO,
        EXPIRY,
        CVV,
        PIN_CODE,
        COUNTRY,
        CITY,
        STATE,
        ADDRESS
    )

    # 5) Assert OTP page
    assert checkout.is_on_otp_page(), "Did not land on OTP page"
