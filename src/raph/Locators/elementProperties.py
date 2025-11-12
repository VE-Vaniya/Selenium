# ElementProperties.py
"""
Author: Abdul Rafay
Topic: Selenium Element Properties & States
Description:
    Demonstrates how to get element properties (text, attributes, size, location)
    and check states (displayed, enabled, selected) in Selenium.
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
driver.get("https://the-internet.herokuapp.com/checkboxes")

# --- 1. Locate checkboxes ---
checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

for i, checkbox in enumerate(checkboxes, start=1):
    print(f"\n--- Checkbox {i} ---")
    print("Displayed?:", checkbox.is_displayed())
    print("Enabled?:", checkbox.is_enabled())
    print("Selected?:", checkbox.is_selected())
    print("Tag Name:", checkbox.tag_name)
    print("Size:", checkbox.size)
    print("Location:", checkbox.location)

    # Toggle checkbox if not selected
    if not checkbox.is_selected():
        checkbox.click()
        print("✅ Checkbox clicked")

time.sleep(1)

# --- 2. Inspect input field attributes ---
driver.get("https://the-internet.herokuapp.com/inputs")
input_field = driver.find_element(By.TAG_NAME, "input")
input_field.send_keys("5678")
print("\nInput Field Properties:")
print("Displayed?:", input_field.is_displayed())
print("Enabled?:", input_field.is_enabled())
print("Value attribute:", input_field.get_attribute("value"))
print("Tag Name:", input_field.tag_name)
print("Size:", input_field.size)
print("Location:", input_field.location)

# --- 3. Inspect flash message after login (optional) ---
driver.get("https://the-internet.herokuapp.com/login")
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CLASS_NAME, "radius").click()
flash_msg = driver.find_element(By.ID, "flash")
print("\nFlash Message Properties:")
print("Displayed?:", flash_msg.is_displayed())
print("Text:", flash_msg.text.strip())
print("Attribute 'class':", flash_msg.get_attribute("class"))
print("Size:", flash_msg.size)
print("Location:", flash_msg.location)

# --- Close browser ---
driver.quit()
print("\n✅ Element properties & states demo completed successfully!")
