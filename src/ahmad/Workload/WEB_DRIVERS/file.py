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

driver.get(os.getenv("WEB_FILE"))

driver.maximize_window()
driver.implicitly_wait(20)

base_path = os.getenv("IMG_PATH") 
full_path = os.path.join(base_path, "img.jpeg")
driver.find_element(By.ID, "uploadFile").send_keys(full_path)
time.sleep(5)

driver.find_element(By.ID, "downloadButton").click()
time.sleep(5)

base_path2= os.getenv("IMG_DOWNLOAD_PATH")
full_path2 = os.path.join(base_path2,"sampleFile.jpeg")
assert os.path.isfile(full_path2), "Download is not completed"
# print("Download is completed")
# if os.path.isfile(full_path2):
# print("Download is completed")

driver.close()