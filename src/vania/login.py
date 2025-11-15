from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/login")

# Enter credentials
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("S!")
driver.find_element(By.CSS_SELECTOR, "button.radius").click()

# Simple if-else check
if "secure" in driver.current_url:
    print("✅ LOGIN SUCCESS - You're on the secure page!")
    result = True
else:
    print("❌ LOGIN FAILED - Still on login page")
    result = False

driver.quit()
print(f"Final result: {result}")