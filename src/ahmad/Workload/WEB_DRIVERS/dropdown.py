from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
from selenium.webdriver.support.ui import Select
import os

driver = webdriver.Chrome()
driver.maximize_window()

#you can replcae driver.get("https://...") like this
#I am reading from env file thats why i did like this
load_dotenv()
driver.get(os.getenv("WEB_CHECKS_LINK"))

#SINGLE DROPDOWN
dropdown = Select(driver.find_element(By.ID,"carBrands")) # for select tags we use Select class
dropdown.select_by_index(1) #starts from 0
dropdown.select_by_value("mercedes")
dropdown.select_by_visible_text("Saab")
# dropdown.deselect_by_index("Saab") #cannot do for single dropdown ---error

#Multi dropdown
multidrop = Select(driver.find_element(By.ID,"multiSelect")) # for select tags we use Select class
print(multidrop.is_multiple) #return is it multi dropdown or single
print(multidrop.all_selected_options) #true if all options are selected in multi dropdown
# multidrop.select_by_index(0)

# options = driver.find_elements(By.XPATH,"//option") # will gives 8 options because 
# single and multi dropdowns all have option tags
options = multidrop.options # so we use options it returns all options of multi dropdown 
# cannot use options with single dropdown

for opt in options:
    multidrop.select_by_visible_text(opt.text) #not in firefox
    # multidrop.select_by_value(opt.get_attribute("value")) so we use value for firefox. 
    # like opt.text is not avail for firefox


time.sleep(2)
multidrop.deselect_all()