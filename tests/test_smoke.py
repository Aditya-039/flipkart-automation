import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_bypass(driver):
    driver.get("https://www.flipkart.com")

    # wait up to 10 s for the login-modal’s “✕” button to disappear
    # that button has classes "_2KpZ6l _2doB4z"
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.CSS_SELECTOR, "button._2KpZ6l._2doB4z"))
    )

    # also assert no "Login" button in the top‐nav
    login_buttons = driver.find_elements(By.XPATH, "//button[text()='Login']")
    assert not login_buttons, "Still seeing a Login button → login bypass failed"
