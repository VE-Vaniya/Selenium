from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()

wait = WebDriverWait(driver, 10)

driver.get("https://google.com")

search = driver.find_element(By.ID, "APjFqb")
search.send_keys("google scholar")

btn = driver.find_element(By.ID, "zgAlFc")
btn.click()

search_sch = driver.find_element(By.ID, "gs_hdr_tsi")
search.send_keys("daniel galin")

lnk = wait.until(EC.visibility_of_element_located((By.ID, "gs_hdr_tsb")))
lnk.click()
