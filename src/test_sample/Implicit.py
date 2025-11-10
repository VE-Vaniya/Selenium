from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox()
driver.implicitly_wait(10)
# driver.implicitly_wait(0)   # for immediate loading

driver.get("https://daraz.pk")

try:
    search_box = driver.find_element("name", "q")
    print("Search box found")
except NoSuchElementException:
    print("Search box not found")

try:
    button = driver.find_element("tag name", "button")
    print("Button found")
except NoSuchElementException:
    print("Button not found")

driver.quit()