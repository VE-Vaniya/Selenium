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


#FORM PATTERN!
#Full Name
# email
# campus single dropdown
# password
# confirm password
# image for upload (optional)

#you can replcae driver.get("https://...") like this
#I am reading from env file thats why i did like this
load_dotenv()
driver.get(os.getenv("WEB_REGISTER"))

driver.maximize_window()
driver.implicitly_wait(20)


FULLNAME=driver.find_element(By.NAME,"fullName")
EMAIL = driver.find_element(By.NAME,"email")
CAMPUSES = Select(driver.find_element(By.NAME,"campusId"))
PASSWORD = driver.find_element(By.NAME,"password")
CONFIRM_PASSWORD = driver.find_element(By.XPATH,"//input[@placeholder='Confirm your password']")
FILE=driver.find_element(By.XPATH,"//input[@type='file']")
SUBMIT = driver = driver.find_element(By.XPATH,"//button[@type='submit']")

# all valid inputs
FULLNAME.send_keys("Muhammad Ahmad Butt")
time.sleep(1)

EMAIL.send_keys("l233059@lhr.nu.edu.pk")
time.sleep(1)

# cannot use values here cuz its disabled in html
#<values disbaled> in that website
CAMPUSES.select_by_visible_text("Lahore")
time.sleep(1)

PASSWORD.send_keys("Hello123@")
time.sleep(1)

CONFIRM_PASSWORD.send_keys("Hello123@")
time.sleep(1)

base_path = os.getenv("IMG_PATH") 
full_path = os.path.join(base_path, "img.jpeg")
FILE.send_keys(full_path)

time.sleep(10)

# password mismatch
FULLNAME.send_keys("Muhammad Ahmad Butt")
time.sleep(1)

EMAIL.send_keys("l233059@lhr.nu.edu.pk")
time.sleep(1)

CAMPUSES.select_by_visible_text("Lahore")
time.sleep(1)

PASSWORD.send_keys("Hello123@")
time.sleep(1)

CONFIRM_PASSWORD.send_keys("Hello123!") #mismatched password
time.sleep(1)

#its just a IMG PATH like C://Users//downloads//img.jpeg
base_path = os.getenv("IMG_PATH") 
full_path = os.path.join(base_path, "img.jpeg")
FILE.send_keys(full_path)
time.sleep(1)

SUBMIT.click()
time.sleep(10)

driver.close()