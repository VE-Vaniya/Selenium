# BasicSetup.py
"""
Author: Abdul Rafay
Topic: Basic WebDriver Setup & Browser Navigation
Description:
    Demonstrates how to install and launch Chrome using Selenium WebDriver.
    Covers driver initialization, navigation, title fetching, and clean quit.
"""
# import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# os.environ['WDM_LOCAL'] = '0'
# os.environ['WDM_LOG_LEVEL'] = '0'
# --- Step 1: Configure browser options ---
options = Options()
options.add_argument("--start-maximized")      # open window maximized
options.add_argument("--disable-infobars")     # remove 'Chrome is being controlled' info bar
options.add_argument("--disable-extensions")   # disable any extensions

# --- Step 2: Set up WebDriver service ---
service = Service(ChromeDriverManager().install())

# ChromeDriverManager() WORKS FOR CHROME VERSIONS UPTO 114

# SO FOR LATER VERSION USE :

# service = Service(ChromeDriverManager(version="latest").install())

# --- Step 3: Launch browser ---
# driver = webdriver.Chrome(service=service, options=options)


driver = webdriver.Chrome()
print("✅ Chrome WebDriver launched successfully!")

# --- Step 4: Basic navigation commands ---
driver.get("https://www.selenium.dev/")
print("Current URL:", driver.current_url)
print("Page Title:", driver.title)

# Navigate actions
driver.back()      # go back (if any history)
driver.forward()   # go forward
driver.refresh()   # reload the page

# --- Step 5: Wait for observation ---
time.sleep(3)

# --- Step 6: Close browser safely ---
driver.quit()
print("✅ Browser closed successfully!")
#--------------------------------------------------------------------


#---------------------------------------------------------------------