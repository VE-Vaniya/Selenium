#Page Load Timeout
from selenium import webdriver

driver = webdriver.Firefox()
driver.set_page_load_timeout(10)  # 10 seconds

try:
    driver.get("https://daraz.com")  # Will timeout if takes >10s  
    
    print("Page loaded successfully")
except:
    print("Page took too long to load") #(If page loading exceeds 10 seconds, it throws TimeoutException.)


driver.quit()




# Page Load Timeout: Sets maximum time for a page to load completely.

# What it does:
# Waits for page to reach "ready" state
# If page takes longer than timeout, stops loading
# Different from element waits

# Page Load Timeout: Waits for the entire PAGE to finish loading (HTML, CSS, JS, images)
# Element Waits: Waits for specific ELEMENTS to be ready (after page loaded)
