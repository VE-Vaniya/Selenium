# BrowserOptions.py
"""
Author: Abdul Rafay
Topic: WebDriver Options & Capabilities
Description:
    Demonstrates advanced browser configuration using Selenium Options.
    Covers headless mode, incognito, window size, position, and user-agent.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# --- Step 1: Configure Chrome options ---
options = Options()

# Headless mode (browser runs in background)
options.add_argument("--headless=new")   # "--headless" for older versions
options.add_argument("--disable-gpu")    # necessary for headless in Windows

# Incognito mode
options.add_argument("--incognito")

# Window size & position
options.add_argument("--window-size=1200,800")
options.add_argument("--window-position=200,100")

# User-agent spoofing (example)
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) CustomAgent/1.0")

# Disable infobars & extensions
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")

# --- Step 2: Setup WebDriver service ---
# service = Service(ChromeDriverManager().install())

# --- Step 3: Launch browser with options ---
driver = webdriver.Chrome(options=options)
print("✅ Chrome WebDriver launched with custom options!")

# --- Step 4: Navigate to a site ---
driver.get("https://www.selenium.dev/")
print("Current URL:", driver.current_url)
print("Page Title:", driver.title)

# --- Step 5: Demonstrate headless wait ---
time.sleep(3)  # headless mode, still wait to let page load

# --- Step 6: Close browser safely ---
driver.quit()
print("✅ Browser closed successfully with options applied!")
