from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox()
driver.get("https://daraz.com")
wait = WebDriverWait(driver, 10)

# Custom condition: Check if button is red AND contains text "Submit"
def button_red_and_has_text(driver):
    button = driver.find_element(By.ID, "myButton")
    color = button.value_of_css_property("background-color")
    text = button.text
    return color == "rgba(255, 0, 0, 1)" and text == "search"

try:
    # Use custom condition
    wait.until(button_red_and_has_text)
    print("Button is red and says 'search'!")
except:
    print("Button never turned red with 'search' text")

driver.quit()