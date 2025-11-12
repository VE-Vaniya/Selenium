# MultiBrowserSetup.py
"""
Author: Abdul Rafay
Topic: Multi-Browser WebDriver Setup
Description:
    Demonstrates how to configure and launch multiple browsers using Selenium.
    Includes Chrome, Firefox, and Edge with WebDriverManager support.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

# --- Step 1: Configure browser options ---
chrome_options = ChromeOptions()
chrome_options.add_argument("--start-maximized")

firefox_options = FirefoxOptions()
firefox_options.add_argument("--width=1200")
firefox_options.add_argument("--height=800")

edge_options = EdgeOptions()
edge_options.add_argument("--start-maximized")

# --- Step 2: Setup WebDriver services ---
# chrome_service = ChromeService(ChromeDriverManager().install())
# firefox_service = FirefoxService(GeckoDriverManager().install())
# edge_service = EdgeService(EdgeChromiumDriverManager().install())

# --- Step 3: Launch browsers ---
print("Launching Chrome...")
chrome_driver = webdriver.Chrome(options=chrome_options)
chrome_driver.get("https://www.selenium.dev/")
print("Chrome Title:", chrome_driver.title)
time.sleep(2)
chrome_driver.quit()
print("✅ Chrome closed")




print("Launching Edge...")
edge_driver = webdriver.Edge(options=edge_options)
edge_driver.get("https://www.selenium.dev/")
print("Edge Title:", edge_driver.title)
time.sleep(2)
edge_driver.quit()
print("✅ Edge closed")

print("Launching Firefox...")
firefox_driver = webdriver.Firefox(options=firefox_options)
firefox_driver.get("https://www.selenium.dev/")
print("Firefox Title:", firefox_driver.title)
time.sleep(2)
firefox_driver.quit()
print("✅ Firefox closed")

