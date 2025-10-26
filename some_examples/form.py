from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

driver.find_element(By.NAME, "my-text").send_keys("Amar Test Input")

driver.find_element(By.NAME, "my-password").send_keys("password123")

dropdown = driver.find_element(By.NAME, "my-select")
for option in dropdown.find_elements(By.TAG_NAME, "option"):
    if option.text == "Option 2":
        option.click()
        break

driver.find_element(By.TAG_NAME, "button").click()

wait = WebDriverWait(driver, 10)
message = wait.until(
    EC.presence_of_element_located((By.TAG_NAME, "h1"))
)

if "Form submitted" in message.text:
    print("Test Passed: Successfully reached confirmation page")
else:
    print("Test Failed: Did not reach confirmation page")

driver.quit()
