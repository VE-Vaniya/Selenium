import sys
from pathlib import Path
import time
from selenium.webdriver.common.by import By

# Ensure src folder is on sys.path so this file can be run from the haseeb folder
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from haseeb.driver_setup import get_driver


def run(query: str = "laptop"):
  
    driver = get_driver(headless=False)
    try:
        driver.get("https://www.amazon.com/")

        # basic search
        search = driver.find_element(By.ID, "twotabsearchtextbox")
        search.clear()
        search.send_keys(query)
        buttons = driver.find_elements(By.ID, "nav-search-submit-button")
        if buttons:
            buttons[0].click()
        else:
            search.submit()

        time.sleep(2)

        # open first product by /dp/ link
        links = driver.find_elements(By.XPATH, "//a[contains(@href, '/dp/')]")
        if not links:
            print("No products found")
            return
        links[0].click()
        time.sleep(2)

        # click add to cart if present
        add = driver.find_elements(By.ID, "add-to-cart-button")
        if add:
            add[0].click()
            print("Clicked Add to Cart")
        else:
            print("Add to Cart button not found")

    finally:
        driver.quit()


if __name__ == "__main__":
    run()
