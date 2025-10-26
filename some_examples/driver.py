from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("https://www.wikipedia.org/")

search_box = driver.find_element(By.ID, "searchInput")
search_box.send_keys("Selenium") # not selenium webdriver
search_box.submit()

time.sleep(3) 

print("current url:", driver.current_url)
print("page title:", driver.title)

assert "Selenium" in driver.title, "Search Box did not return the expected result"

print("Test Passed: 'Selenium' found in the page title.")

driver.quit()
