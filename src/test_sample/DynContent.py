# Handling Dynamic Content Loading

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://daraz.pk")
wait = WebDriverWait(driver, 10)

try:
    # Wait for search box to be present
    search_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#q")))
    print("✓ Search box loaded")
    
    # Type in search box
    search_box.send_keys("mobile")
    print("✓ Text entered in search box")
    
    # Click search button
    search_btn = driver.find_element(By.CSS_SELECTOR, ".search-box__button--1oH7")
    search_btn.click()
    print("✓ Search button clicked")
    
    # Wait for results to load
    results = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.Bm3ON:nth-child(2)")))
    print("✓ Search results loaded")
    
except Exception as e:
    print(f"✗ Error: {e}")

driver.quit()

# What it is:
# Content that loads AFTER the initial page load
# Elements that appear based on user action
# AJAX calls, lazy loading, form submissions

# Why wait for it:
# Elements may not be immediately available
# Prevents "ElementNotfound" errors
# Ensures page is ready for interaction




