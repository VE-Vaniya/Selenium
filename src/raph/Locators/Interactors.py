# BasicInteractions.py
"""
Author: Abdul Rafay
Topic: Selenium Basic Interactions
Description:
    Demonstrates typing, clicking, clearing, submitting, and reading properties.
    Also checks element states like visibility, enabled status, and selection.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# --- Setup WebDriver ---
options = Options()
options.add_argument("--start-maximized")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=options)

# --- Open demo website ---
driver.get("https://the-internet.herokuapp.com/login")

# --- 1. Typing into input fields ---
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")

username.send_keys("tomsmith")
password.send_keys("SuperSecretPassword!")
print("✅ Typed username and password")

time.sleep(1)

# --- 2. Clicking button ---
login_button = driver.find_element(By.CLASS_NAME, "radius")
login_button.click()
print("✅ Clicked login button")

time.sleep(1)

# --- 3. Reading element properties ---
flash_msg = driver.find_element(By.ID, "flash")
print("Flash Message Text:", flash_msg.text.strip())
print("Displayed?", flash_msg.is_displayed())
print("Enabled?", flash_msg.is_enabled())

# --- 4. Checking checkbox / radio button states ---
# Navigate to checkboxes page
driver.get("https://the-internet.herokuapp.com/checkboxes")
checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

for i, checkbox in enumerate(checkboxes, start=1):
    print(f"Checkbox {i} selected?:", checkbox.is_selected())
    if not checkbox.is_selected():
        checkbox.click()  # Select it
        print(f"Checkbox {i} clicked to select")

time.sleep(1)

# --- 5. Clearing input fields ---
driver.get("https://the-internet.herokuapp.com/inputs")
input_field = driver.find_element(By.TAG_NAME, "input")
input_field.send_keys("12345")
time.sleep(1)
input_field.clear()
print("✅ Input field cleared")

# --- Close browser ---
driver.quit()
print("✅ Basic interactions demo completed successfully!")
