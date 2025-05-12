import pickle
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# 1. Launch Chrome and navigate to Flipkart
opts = Options()
opts.add_argument("--start-maximized")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=opts)
driver.get("https://www.flipkart.com")

# 2. Pause for you to log in manually (enter phone, OTP, etc.)
input("❗️ Log in to Flipkart now, then press Enter to continue...")

# 3. Save all cookies to a file
pickle.dump(driver.get_cookies(), open("flipkart_cookies.pkl", "wb"))
print("✅ Cookies saved to flipkart_cookies.pkl")

driver.quit()
