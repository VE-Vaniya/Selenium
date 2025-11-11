from selenium import webdriver
from dotenv import load_dotenv
import os
import time

load_dotenv()

#instanciate the driver
driver = webdriver.Firefox()

#open a url
driver.get(os.getenv("WEB_PREVIEW"))
driver.get(os.getenv("WEB_LOGIN"))
driver.back()
driver.forward()
driver.refresh()

time.sleep(10)

#close the driver
driver.quit()