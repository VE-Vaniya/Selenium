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
driver.implicitly_wait(20)

load_dotenv()

driver.get(os.getenv("WEB_DATE"))

BOXy = driver.find_element(By.CLASS_NAME,"dIEany")
BOXy.click()
#14 JAN - 14 FEB
NEXT_BTN = driver.find_element(By.XPATH,"//span[@data-testid='calendarRightArrowBtn']")

CHECK_IN = driver.find_element(By.XPATH,"//span[@data-testid='date_14_0_2026']")
CHECK_OUT = driver.find_element(By.XPATH,"//span[@data-testid='date_14_1_2026']")

NEXT_BTN.click()
time.sleep(1)
NEXT_BTN.click()
time.sleep(1)
CHECK_IN.click()
time.sleep(1)
CHECK_OUT.click()
time.sleep(5)

driver.close()