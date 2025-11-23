from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://daraz.pk")
wait = WebDriverWait(driver, 10)

try:
    # 1. Check if search box is clickable
    search_box = wait.until(EC.element_to_be_clickable((By.NAME, "q")))
    print("✓ Search box is clickable")
except:
    print("✗ Search box not clickable")

try:
    # 2. Check if search box is present
    element = wait.until(EC.presence_of_element_located((By.NAME, "q")))
    print("✓ Search box is present")
except:
    print("✗ Search box not present")

try:
    # 3. Check if search box is visible
    visible_element = wait.until(EC.visibility_of_element_located((By.NAME, "q")))
    print("✓ Search box is visible")
except:
    print("✗ Search box not visible")

try:
    # 4. Check if page contains "Daraz" in title
    title_check = wait.until(EC.title_contains("Daraz"))
    print("✓ Page title contains 'Daraz'")
except:
    print("✗ Page title doesn't contain 'Daraz'")

driver.quit()