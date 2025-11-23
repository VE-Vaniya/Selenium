from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)

try:
    # 1. AJAX Content
    driver.find_element(By.ID, "load-more").click()
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "new-item")))
    print("✓ AJAX content loaded")
except:
    print("✗ AJAX content failed to load")

try:
    # 2. Lazy Loading
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "lazy-image")))
    print("✓ Lazy content loaded")
except:
    print("✗ Lazy content failed to load")

try:
    # 3. Form Submission
    old_page = driver.find_element(By.TAG_NAME, "html")
    driver.find_element(By.ID, "submit").click()
    wait.until(EC.staleness_of(old_page))
    print("✓ Form submitted successfully")
except:
    print("✗ Form submission failed")

try:
    # 4. Auto-complete
    search_box = driver.find_element(By.ID, "search")
    search_box.send_keys("laptop")
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "suggestion-item")))
    print("✓ Auto-complete loaded")
except:
    print("✗ Auto-complete failed")

try:
    # 5. Progress Spinner
    wait.until(EC.invisibility_of_element((By.ID, "loading-spinner")))
    print("✓ Loading completed")
except:
    print("✗ Loading spinner didn't disappear")

try:
    # 6. Dynamic Text
    wait.until(EC.text_to_be_present_in_element((By.ID, "status"), "Completed"))
    print("✓ Status updated to 'Completed'")
except:
    print("✗ Status never updated")

driver.quit()