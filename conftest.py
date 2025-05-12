import os, pickle, pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="session")
def driver():
    opts = Options()
    # core opts
    opts.add_argument("--start-maximized")
    # remove the “Chrome is being controlled…” infobar
    opts.add_experimental_option("excludeSwitches", ["enable-automation"])
    opts.add_experimental_option("useAutomationExtension", False)
    # disable the navigator.webdriver flag
    opts.add_argument("--disable-blink-features=AutomationControlled")
    # optional: set a real-browser user-agent
    opts.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/114.0.5735.199 Safari/537.36"
    )

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=opts)

    # inject before any page loads
    driver.execute_cdp_cmd(
        "Page.addScriptToEvaluateOnNewDocument",
        {
            "source": """
                Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
            """
        },
    )

    # load cookies for login bypass
    driver.get("https://www.flipkart.com")
    cookie_file = os.path.join(os.getcwd(), "flipkart_cookies.pkl")
    if os.path.exists(cookie_file):
        for c in pickle.load(open(cookie_file, "rb")):
            driver.add_cookie(c)
        driver.refresh()

    yield driver
    driver.quit()


