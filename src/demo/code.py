from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)

try:
    driver.get("https://www.saucedemo.com/")

    #login
    wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()


    #wait for home page
    wait.until(EC.presence_of_element_located((By.ID, "add-to-cart-sauce-labs-backpack")))
    Select(driver.find_element(By.CLASS_NAME, "product_sort_container")).select_by_value("az")  #for drop down multiple and single select
    
    
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()    
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    driver.find_element(By.ID, "checkout").click()


    #driver.find_element(By.ID, "first-name").send_keys("John")
    wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys("John")
    driver.find_element(By.ID, "last-name").send_keys("Doe")
    driver.find_element(By.ID, "postal-code").send_keys("12345")

    driver.find_element(By.ID, "continue").click()

    time.sleep(5)
    wait.until(EC.presence_of_element_located((By.ID,"finish"))).click()
    time.sleep(5)
    wait.until(EC.presence_of_element_located((By.ID,"back-to-products"))).click()


    time.sleep(100)

    print("Login successful")
except:
    print("Login failed")