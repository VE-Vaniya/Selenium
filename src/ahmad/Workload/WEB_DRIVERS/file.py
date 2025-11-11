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
driver.get(os.getenv("WEB_FILE"))

driver.maximize_window()
driver.implicitly_wait(20)

#its just a IMG PATH like C://Users//downloads//img.jpeg
base_path = os.getenv("IMG_PATH") 
full_path = os.path.join(base_path, "img.jpeg")

driver.find_element(By.ID, "uploadFile").send_keys(full_path)
time.sleep(5)

driver.find_element(By.ID, "downloadButton").click()
time.sleep(5)

#its just a IMG PATH like C://Users//downloads//sampleFile.jpeg
base_path2= os.getenv("IMG_DOWNLOAD_PATH")
full_path2 = os.path.join(base_path2,"sampleFile.jpeg")

if os.path.isfile(full_path2):
    print("Download is completed")
else:
    print("Download is not completed!")

driver.close()