from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
from selenium.webdriver.support.ui import Select
import os

driver = webdriver.Chrome()
driver.maximize_window()

load_dotenv()

driver.get(os.getenv("WEB_CHECKS_LINK"))

#SINGLE DROPDOWN
# dropdown = Select(driver.find_element(By.ID,"carBrands"))
# dropdown.select_by_index(1)
# dropdown.select_by_value("mercedes")
# dropdown.select_by_visible_text("Saab")

# dropdown.deselect_by_index("Saab") #cannot do for single dropdown ---error

#Multi dropdown
multidrop = Select(driver.find_element(By.ID,"multiSelect"))
print(multidrop.is_multiple)
print(multidrop.all_selected_options)
# multidrop.select_by_index(0)

# options = driver.find_elements(By.XPATH,"//option") # will gives 8 options single + multi
options = multidrop.options

# optArr = [opt.text for opt in options]
# optArr = [opt.get_attribute("value") for opt in options]

for opt in options:
    # optArr= opt.text
    # multidrop.select_by_value(opt.get_attribute("value"))
    # print("selected",optArr)
    multidrop.select_by_visible_text(opt.text) #not in firefox

# print(optArr)

time.sleep(2)

multidrop.deselect_all()


