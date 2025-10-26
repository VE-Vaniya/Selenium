import sys
from pathlib import Path
import time
from selenium.webdriver.common.by import By

# Ensure repo src is on sys.path so it can be run from this folder
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from haseeb.driver_setup import get_driver


def search_products(query: str = "usb flash drive"):
    driver = get_driver(headless=False)
    driver.get("https://www.amazon.com/")

    # Search for the product
    search = driver.find_element(By.ID, "twotabsearchtextbox")
    search.clear()
    search.send_keys(query)
    search.submit()

    # Just wait a bit so results load (and browser stays open)
    time.sleep(5)

    # Do not quit — keep browser open
    print(f"Searched for '{query}' on Amazon.")


if __name__ == "__main__":
    search_products()
