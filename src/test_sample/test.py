#for selenium web
from selenium import webdriver
from selenium.webdriver.common.by import By

# Selenium automatically manages ChromeDriver (version 4.6+)
driver = webdriver.Chrome()

driver.get("https://techwithtim.net")
print(f"Page title: {driver.title}")

# Your test code continues here...
driver.quit()