import sys
from pathlib import Path

# Simple script: ensure repo src is on sys.path so it can be run from this folder
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from haseeb.driver_setup import get_driver
from selenium.webdriver.common.by import By
import time


def run(query: str = "usb flash drive"):
    driver = get_driver(headless=False)
    driver.get("https://www.amazon.com/")
    search = driver.find_element(By.ID, "twotabsearchtextbox")
    search.clear()
    search.send_keys(query)
    search.submit()
    time.sleep(2)
    results = driver.find_elements(By.CSS_SELECTOR, "div.s-main-slot div[data-component-type='s-search-result'] h2 a")
    if not results:
        print("No results found")
        driver.quit()
        return
    results[0].click()
    time.sleep(2)
    add_btns = driver.find_elements(By.ID, "add-to-cart-button")
    if add_btns:
        add_btns[0].click()
        print("Clicked Add to Cart")
    else:
        print("Add to Cart button not found")
    driver.quit()


if __name__ == "__main__":
    run()
