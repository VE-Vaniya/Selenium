from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains # for mouse events
import time

driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()
handles = driver.window_handles
driver.switch_to.window(handles[-1])
time.sleep(0.7)
print(driver.title)
time.sleep(0.7)
driver.close()
driver.switch_to.window(handles[0])
