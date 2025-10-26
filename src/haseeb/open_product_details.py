import sys
from pathlib import Path
import time
from selenium.webdriver.common.by import By

# Ensure repo src is on sys.path so we can import the package when running
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from haseeb.driver_setup import get_driver


def run(query: str = "laptop"):
    
    driver = get_driver(headless=False)
    try:
        driver.get("https://www.amazon.com/")

        search = driver.find_element(By.ID, "twotabsearchtextbox")
        search.clear()
        search.send_keys(query)

        buttons = driver.find_elements(By.ID, "nav-search-submit-button")
        if buttons:
            buttons[0].click()
        else:
            search.submit()

        time.sleep(2)

        # find product links (they usually contain '/dp/') and open the first
        links = driver.find_elements(By.XPATH, "//a[contains(@href, '/dp/')]")
        if not links:
            print("No products found")
            return

        links[0].click()
        time.sleep(2)

        # read title and price if present (simple checks to avoid exceptions)
        title = "n/a"
        if driver.find_elements(By.ID, "productTitle"):
            title = driver.find_element(By.ID, "productTitle").text


        print("Product title:", title)
        print("Price:", price)

    finally:
        driver.quit()


if __name__ == "__main__":
    run()
