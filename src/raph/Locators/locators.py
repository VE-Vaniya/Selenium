# # LocatorsDemo.py
# """
# Author: Abdul Rafay
# Topic: Selenium Element Locators
# Description:
#     Demonstrates all types of element locators in Selenium and basic verification.
# """

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# import time

# # --- Setup WebDriver ---
# options = Options()
# options.add_argument("--start-maximized")
# # service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome( options=options)

# # --- Open demo website ---
# driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")

# # --- Wait until input is visible ---
# wait = WebDriverWait(driver, 10)  # wait up to 10 seconds

# # --- Close modal popup if it appears ---
# try:
#     modal_close = wait.until(EC.element_to_be_clickable((By.ID, "at-cv-lightbox-close")))
#     modal_close.click()
#     print("Popup closed")
# except:
#     print("No popup found")


# user_input = wait.until(EC.visibility_of_element_located((By.ID, "user-message")))


# # --- 1. By ID ---
# user_input = driver.find_element(By.ID, "user-message")
# user_input.send_keys("Hello from ID locator!")
# time.sleep(1)

# # --- 2. By Name ---
# show_button = driver.find_element(By.NAME, "submit")
# show_button.click()
# time.sleep(1)

# # --- 3. By Class Name ---
# header = driver.find_element(By.CLASS_NAME, "panel-heading")
# print("Header Text:", header.text)

# # --- 4. By Tag Name ---
# paragraph = driver.find_element(By.TAG_NAME, "p")
# print("Paragraph text:", paragraph.text)

# # --- 5. By Link Text ---
# link = driver.find_element(By.LINK_TEXT, "Selenium Easy")
# print("Link Text:", link.text)

# # --- 6. By Partial Link Text ---
# partial_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Selenium")
# print("Partial Link Text:", partial_link.text)

# # --- 7. By CSS Selector ---
# css_input = driver.find_element(By.CSS_SELECTOR, "input#user-message")
# css_input.clear()
# css_input.send_keys("Hello via CSS Selector")
# time.sleep(1)

# # --- 8. By XPath ---
# xpath_input = driver.find_element(By.XPATH, "//input[@id='user-message']")
# xpath_input.clear()
# xpath_input.send_keys("Hello via XPath")
# time.sleep(1)

# # --- Close browser ---
# driver.quit()
# print("✅ Locator demo completed successfully!")


# LocatorsDemo.py
"""
Author: Abdul Rafay
Topic: Selenium Element Locators
Description:
    Demonstrates all types of element locators in Selenium using https://the-internet.herokuapp.com/.
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
# service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome( options=options)

# --- Open demo website ---
driver.get("https://the-internet.herokuapp.com/login")

# --- 1. By ID ---
username = driver.find_element(By.ID, "username")
username.send_keys("tomsmith")
time.sleep(1)

# --- 2. By Name ---
password = driver.find_element(By.NAME, "password")
password.send_keys("SuperSecretPassword!")
time.sleep(1)

# --- 3. By Class Name ---
login_button = driver.find_element(By.CLASS_NAME, "radius")
login_button.click()
time.sleep(1)

# --- 4. By Tag Name ---
header = driver.find_element(By.TAG_NAME, "h2")
print("Header Text:", header.text)

# --- 5. By Link Text ---
logout_link = driver.find_element(By.LINK_TEXT, "Logout")
print("Logout Link Text:", logout_link.text)

# --- 6. By Partial Link Text ---
partial_logout = driver.find_element(By.PARTIAL_LINK_TEXT, "Log")
print("Partial Link Text:", partial_logout.text)

# --- 7. By CSS Selector ---
flash_msg = driver.find_element(By.CSS_SELECTOR, "div#flash")
print("Flash message (CSS):", flash_msg.text.strip())

# --- 8. By XPath ---
flash_msg_xpath = driver.find_element(By.XPATH, "//div[@id='flash']")
print("Flash message (XPath):", flash_msg_xpath.text.strip())

# --- Close browser ---
driver.quit()
print("✅ Locator demo completed successfully on Herokuapp!")
