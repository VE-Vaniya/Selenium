"""
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.google.com")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("selenium webdriver example")
search_box.submit()

driver.quit()

No separate server needed.
Uses real browser automation.
Uses locators like:
By.ID, By.NAME, By.XPATH, etc.

======================================================= RC
from selenium import selenium
sel = selenium("localhost", 4444, "*chrome", "https://www.google.com")

sel.start()
sel.open("/")
sel.type("name=q", "selenium rc example")
sel.click("name=btnK")
sel.wait_for_page_to_load("3000")
sel.stop()

Must start RC server manually.
Browser controlled through JavaScript injection.
Uses old methods:
open(), type(), click(), wait_for_page_to_load()
"""