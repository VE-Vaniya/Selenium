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

load_dotenv()

driver.get(os.getenv("WEB_KEYS"))

driver.maximize_window()
driver.implicitly_wait(20)

input_area = driver.find_element(By.XPATH, "//*[@class='ql-editor ql-blank']")
input_area.send_keys("NIGGA!!!")

act = ActionChains(driver)
#select text ctrl + A
act.key_down(Keys.CONTROL)
act.send_keys("a")
act.key_up(Keys.CONTROL)
act.perform()

#copy the text ctrl + C
act.key_down(Keys.CONTROL)
act.send_keys("c")
act.key_up(Keys.CONTROL)
act.perform()

# press right arrow key
act.send_keys(Keys.ARROW_RIGHT)
time.sleep(2)
#press Enter key
act.send_keys(Keys.ENTER)
time.sleep(3)
#paste the text by ctrl + V
act.key_down(Keys.CONTROL)
act.send_keys("v")
act.key_up(Keys.CONTROL)
act.perform()

time.sleep(5)

driver.close()