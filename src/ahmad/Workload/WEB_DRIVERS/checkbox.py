from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os

driver = webdriver.Firefox()
driver.maximize_window()

load_dotenv()

driver.get(os.getenv("WEB_CHECKS_LINK"))
print("TITLE: ",driver.title)
print("URL: ",driver.current_url) # for chrome its content_url


# checkBox_ford = driver.find_element(By.ID,"option1")
# checkBox_ford.click()

# checkBox_ford = driver.find_element(By.ID,"option2")
# checkBox_ford.click()

# checkBox_ford = driver.find_element(By.ID,"option3")
# checkBox_ford.click()

checkBoxs = driver.find_elements(By.XPATH,"//input[@type='checkbox']")

for checkBox in checkBoxs:
    if not checkBox.is_selected():
        checkBox.click()

time.sleep(10)

driver.close()

