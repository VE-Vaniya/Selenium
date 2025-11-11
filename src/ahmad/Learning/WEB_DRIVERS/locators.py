from selenium import webdriver
from dotenv import load_dotenv
import os
import time
from selenium.webdriver.common.by import By

load_dotenv()

#instanciate the driver
driver = webdriver.Firefox()

#open a url
driver.get(os.getenv("WEB_DEMO"))
driver.maximize_window()

time.sleep(3)

driver.find_element(By.ID, "user-name").send_keys("standard_user")
time.sleep(1)

password = driver.find_element(By.XPATH, "//input[@id='password']")
# password = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
# password = driver.find_element(By.XPATH, "//input[starts-with(@id,'pass')]")
# password = driver.find_element(By.XPATH, "//input[ends-with(@id,'word')]")
# product = driver.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']")
# product = driver.find_element(By.XPATH, "//div[contains(text(),'Backpack')]")
# password = driver.find_element(By.XPATH, "//input[@type='password'] and @id='password']") #and or
# password = driver.find_element(By.XPATH, "//input[2]" ) #indexing starts from 1
# product = driver.find_element(By.LINK_TEXT, "Sauce Labs Backpack") 

password.send_keys("secret_sauce")
time.sleep(1)

driver.find_element(By.CLASS_NAME, "btn_action").click()
time.sleep(3)

driver.quit()