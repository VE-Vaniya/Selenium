# AdvancedInteractions.py
"""
Author: Abdul Rafay
Topic: Selenium Advanced Interactions & Popups
Description:
    Demonstrates handling alerts, frames/iframes, multiple windows,
    and basic mouse interactions.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# --- Setup WebDriver ---
options = Options()
options.add_argument("--start-maximized")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=options)

# --- 1. Handling Alerts ---
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# Alert 1: Simple alert
alert_btn = driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']")
alert_btn.click()
alert = driver.switch_to.alert
print("Alert Text:", alert.text)
alert.accept()
print("✅ Simple alert accepted")
time.sleep(1)

# Alert 2: Confirm alert
confirm_btn = driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']")
confirm_btn.click()
alert = driver.switch_to.alert
print("Confirm Text:", alert.text)
alert.dismiss()
print("✅ Confirm alert dismissed")
time.sleep(1)

# Alert 3: Prompt alert
prompt_btn = driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']")
prompt_btn.click()
alert = driver.switch_to.alert
alert.send_keys("Hello Selenium")
alert.accept()
print("✅ Prompt alert handled")
time.sleep(1)

# --- 2. Handling Frames/Iframes ---
driver.get("https://the-internet.herokuapp.com/iframe")
iframe = driver.find_element(By.ID, "mce_0_ifr")
driver.switch_to.frame(iframe)
editor = driver.find_element(By.ID, "tinymce")
# editor.clear()

#BASICALLY THERES DIFF IN TEXT FIELDS EDITOR ONE IS A RICH TXT FIELD SO HERE THE OPTIONS ARE TO CLEAR THRU KEY ACTIONS
editor.send_keys(Keys.BACKSPACE) 

editor.send_keys("Hello from Selenium iframe!")
print("✅ Typed inside iframe")
driver.switch_to.default_content()  # return to main page

# --- 3. Handling Multiple Windows/Tabs ---
driver.get("https://the-internet.herokuapp.com/windows")
main_window = driver.current_window_handle
driver.find_element(By.LINK_TEXT, "Click Here").click()

all_windows = driver.window_handles
for window in all_windows:
    if window != main_window:
        driver.switch_to.window(window)
        print("New Window Title:", driver.title)
        driver.close()

driver.switch_to.window(main_window)
print("✅ Returned to main window:", driver.title)

# --- 4. Mouse Actions ---
driver.get("https://the-internet.herokuapp.com/hovers")
hover_images = driver.find_elements(By.CLASS_NAME, "figure")
actions = ActionChains(driver)

for i, img in enumerate(hover_images, start=1):
    actions.move_to_element(img).perform()
    print(f"Hovered over image {i}")
    time.sleep(1)

# --- Close browser ---
driver.quit()
print("✅ Advanced interactions & popups demo completed successfully!")
