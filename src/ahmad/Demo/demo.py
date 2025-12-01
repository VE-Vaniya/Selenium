import os
import pytest
import requests
import sys
import time
from dotenv import load_dotenv
from pathlib import Path
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException,StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait

load_dotenv()

driver = webdriver.Chrome()
driver.maximize_window()

driver.get(f"http://{os.getenv('IP')}:5500/website/index.html")

wait = WebDriverWait(driver,10)

try:
    parent_id = driver.current_window_handle
    name = wait.until(
    EC.visibility_of_element_located(
        (By.ID,"username")
    )
)
    name.send_keys("test")

    passs = wait.until(
    EC.visibility_of_element_located(
        (By.ID,"password")
    )
)
    passs.send_keys("123")

    wait.until(
    EC.element_to_be_clickable(
        (By.CLASS_NAME,"btn")
    )
).click()
    
#empty cart
    cart = wait.until(
    EC.element_to_be_clickable(
        (By.ID,"cart-btn")
    )
)
    cart.click()

    # time.sleep(10)
    checkout = wait.until(
    EC.visibility_of_element_located(
        (By.ID,"checkout-btn")
    )
)
   
    checkout.click()
    time.sleep(1)
    al= driver.switch_to.alert
    al.accept()

    closeBtn = wait.until(
    EC.visibility_of_element_located(
        (By.ID,"close-cart")
    )  
  )
    
    closeBtn.click()


    products = wait.until(
        EC.visibility_of_all_elements_located(
            (By.CLASS_NAME,"product-card")
        )
    )

    i =0 
    for prod in products:
        if i%2==0:
            prod.find_element(By.CLASS_NAME,"btn").click()
        i=i+1
        
    cart = wait.until(
    EC.element_to_be_clickable(
        (By.ID,"cart-btn")
    )
)
    cart.click()

    # time.sleep(10)
    checkout = wait.until(
    EC.visibility_of_element_located(
        (By.ID,"checkout-btn")
    )
)
 
    # print(driver.current_window_handle)
    checkout.click()
    time.sleep(1)
    
    # print(driver.current_window_handle)
    # print(driver.window_handles)
    
    time.sleep(2)
    win = driver.window_handles
    for i in win:
        if i != parent_id:
            print(i)
            print(parent_id)
            driver.switch_to.window(i)
            print("swi")
            
    time.sleep(2)
    iframe = wait.until(
        EC.presence_of_element_located(
            (By.CLASS_NAME,"checkout-iframe")
        )
    )
    
    driver.switch_to.frame(iframe)
    #FORM FILL
    wait.until(
        EC.visibility_of_element_located(
            (By.ID,"firstName")
        )
    ).send_keys("Name")
    
    wait.until(
        EC.visibility_of_element_located(
            (By.ID,"lastName")
        )
    ).send_keys("Last")
    
    wait.until(
        EC.visibility_of_element_located(
            (By.ID,"postalCode")
        )
    ).send_keys("1001")
    
    sel = wait.until(
        EC.visibility_of_element_located(
            (By.ID,"deliveryType")
        )
    )
    
    Select(sel).select_by_value("premium")
    
    selMulti = wait.until(
        EC.visibility_of_element_located(
            (By.ID,"coupons")
        )
    )
    
    s = Select(selMulti)
    s.select_by_index(0)
    s.select_by_index(2)
    s.select_by_index(4)
    
    tagMulti = wait.until(
        EC.visibility_of_element_located(
            (By.ID,"tags")
        )
    )
    
    t = Select(tagMulti)
    t.select_by_index(0)
    t.select_by_index(2)
    t.select_by_index(4)
    
    wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME,"btn")
        )
    ).click()
    
    
    al = wait.until(EC.alert_is_present())
    al.send_keys("1100")
    al.accept()    
    al.accept()
    
    print("b")
    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH,"//button[text()='Back to Home']")
        )
    ).click()
    print("a")
    
    driver.switch_to.default_content()
    time.sleep(2)
    
    time.sleep(2)
    driver.switch_to.window(parent_id)


except:
    print("Test failed!")




time.sleep(5)

driver.quit()