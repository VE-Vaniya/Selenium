from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

driver = webdriver.Firefox()
driver.get("https://daraz.pk")

# Fluent wait: check every 3 seconds, ignore temporary errors
wait = WebDriverWait(
    driver, 
    timeout=15,    #Wait max 15 seconds
    poll_frequency=3,   #check every 3 seconds (default is 0.5 seconds)
    ignored_exceptions=[NoSuchElementException, StaleElementReferenceException]   #Ignore these exceptions 
)

try:
    # This handles elements that appear/disappear randomly
    element = wait.until(EC.element_to_be_clickable((By.ID, "myButton")))   
    print("✓ Element found and clickable")
except:
    print("✗ Element not found within 15 seconds")

driver.quit()