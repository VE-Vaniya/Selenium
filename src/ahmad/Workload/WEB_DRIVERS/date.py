from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from dotenv import load_dotenv
from selenium.webdriver.support.ui import Select
import os

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(60)

#you can replcae driver.get("https://...") like this
#I am reading from env file thats why i did like this
load_dotenv()
driver.get(os.getenv("WEB_DATE"))

DateField = driver.find_element(By.CLASS_NAME,"hasDatepicker")
DateField.click()
time.sleep(1)

# Click previous month button 11 times
# actually its nov 2025 i want to select dec 2024
PrevBtn = driver.find_element(By.XPATH,"//a[@class='ui-datepicker-prev ui-corner-all']")
for i in range(11):
    PrevBtn.click()
    time.sleep(0.5)

# selected 11 dec 2024
Datee = driver.find_element(By.XPATH,"//a[text()='11']")
Datee.click()
time.sleep(1)

driver.close()