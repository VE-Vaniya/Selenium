from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/iframe")

frame = driver.find_element(By.ID, "mce_0_ifr")
driver.switch_to.frame(frame) 

editor = driver.find_element(By.ID, "tinymce")  # now Selenium is inside frame ayo nahhhh
editor.clear()
editor.send_keys("Hello from Selenium!")

driver.switch_to.default_content()  # going back to main page

time.sleep(0.7)
driver.quit()
