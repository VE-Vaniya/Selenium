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

#you can replcae driver.get("https://...") like this
#I am reading from env file thats why i did like this
load_dotenv()
driver.get(os.getenv("WEB_KEYS"))

driver.maximize_window()
driver.implicitly_wait(20)

input_area = driver.find_element(By.XPATH, "//*[@class='ql-editor ql-blank']")
input_area.send_keys("NIGGA!!!")

#Scenario: selecting all text then copy it then clicking right key then pressing enter key than pasting

act = ActionChains(driver) #action chain

#select text ctrl + A
act.key_down(Keys.CONTROL)
act.send_keys("a")
act.key_up(Keys.CONTROL)
act.perform() # used when we use either key_down or up

#copy the text ctrl + C
act.key_down(Keys.CONTROL)
act.send_keys("c")
act.key_up(Keys.CONTROL)
act.perform() # used when we use either key_down or up

# press right arrow key
act.send_keys(Keys.ARROW_RIGHT) # here didnot use key down and up so, no perform func
time.sleep(2)

#press Enter key
act.send_keys(Keys.ENTER) # here didnot use key down and up so, no perform func
time.sleep(3)

#paste the text by ctrl + V
act.key_down(Keys.CONTROL)
act.send_keys("v")
act.key_up(Keys.CONTROL)
act.perform() # used when we use either key_down or up

time.sleep(5)
driver.close()