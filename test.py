import os
import pytest
import requests
import sys
import time
from dotenv import load_dotenv
from pathlib import Path
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException,StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.nu.edu.pk/")


wait = WebDriverWait(driver,20)
ad = wait.until(
EC.visibility_of_element_located(
    (By.XPATH,"//a[@class='main-menu' and text()='Admissions']")
)
)

ad.click()

adm = wait.until(
EC.visibility_of_element_located(
    (By.XPATH,"//a[@class='link-page' and text()='Admission Schedule']")
)
)

adm.click()

wait.until(
    EC.visibility_of_element_located(
        (By.CLASS_NAME,"button-search")
    )
).click()

wait.until(
EC.visibility_of_element_located(
    (By.NAME,"search")
)
).send_keys("cs")

# wait.until(
# EC.visibility_of_element_located(
#     (By.CLASS_NAME,"gsc-search-button-v2")
# )
# ).click()

srchs = wait.until(
EC.visibility_of_element_located(
    (By.XPATH,"//a[@class='gs-title' and @dir='ltr']")
)
)

ii=0
print(len(srchs))
for i in srchs:
    print(ii)
    if ii == 3: 
        break
    print(i.text)
    ii=ii+1

time.sleep(5)

driver.quit()