from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os

driver = webdriver.Firefox()
driver.maximize_window()

#you can replcae driver.get("https://...") like this
#I am reading from env file thats why i did like this
load_dotenv()
driver.get(os.getenv("WEB_CHECKS_LINK"))

#methods to get url and title of website
print("TITLE: ",driver.title)
print("URL: ",driver.current_url) # for chrome its content_url


radio_ford = driver.find_element(By.ID,"radio1")
radio_ford.click()


radios = driver.find_elements(By.XPATH,"//input[@type='radio']")
for r in radios:
    if not r.is_selected():
        time.sleep(0.5)
        r.click()

radios = driver.find_elements(By.XPATH,"//label[@for='radio1']")
for r in radios:
    print("Before:", r.text)
    driver.execute_script("arguments[0].textContent = 'Updated Radio Label';", r)
    print("After:", r.text)


time.sleep(10)
driver.close()