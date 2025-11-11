from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains # for mouse events
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)

# hover mouse event
driver.get("https://the-internet.herokuapp.com/hovers")
hover_element = driver.find_element(By.XPATH, "//img[@src='/img/avatar-blank.jpg']")
actions = ActionChains(driver)
actions.move_to_element(hover_element).perform()

profile_Text = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='figcaption']")))
print(profile_Text.text)

driver.quit()

# right click mouse event
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
click_element = driver.find_element(By.CSS_SELECTOR, ".context-menu-one")
actions = ActionChains(driver)
actions.context_click(click_element).perform()

copy_button = wait.until(EC.presence_of_element_located(((By.CSS_SELECTOR, ".context-menu-icon-copy")))
print(copy_button.text)
driver.quit()

# double click
driver.get("https://api.jquery.com/dblclick/")
click_element = driver.find_element(By.TAG_NAME, "div")
actions = ActionChains(driver)
actions.double_click(click_element).perform()
time.sleep(2)
driver.quit()

# drag and drop mouse event (could not find an example right now without js workaround)
driver.get("https://the-internet.herokuapp.com/drag_and_drop") 
src = driver.find_element(By.ID, "column-a")
dst = driver.find_element(By.ID, "column-b")
actions = ActionChains(driver)
actions.drag_and_drop(src, dst).perform()
time.sleep(0.5)
driver.quit()


