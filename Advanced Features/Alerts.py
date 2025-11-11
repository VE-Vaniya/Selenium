from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains # for mouse events
import time

# browser dialogs are same as js alerts so that also gets covered here

driver = webdriver.Firefox()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
a = driver.switch_to.alert # switch_to.confirm and click the button || switch_to.prompt and send keys to the input field

print(a.text)
a.accept()
