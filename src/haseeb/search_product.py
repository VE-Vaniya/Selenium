import sys
from pathlib import Path

# Ensure src folder is on sys.path when running directly from this folder
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from .driver_setup import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def run(query: str = "laptop"):
    driver = get_driver(headless=True)
    driver.get("https://www.amazon.com/")
    search = driver.find_element(By.ID, "twotabsearchtextbox")
    search.clear()
    search.send_keys(query)
    search.send_keys(Keys.ENTER)
    time.sleep(2)
    results = driver.find_elements(By.CSS_SELECTOR, "div.s-main-slot div[data-component-type='s-search-result'] h2 a span")
    print(f"Search results for '{query}':")
    for i, r in enumerate(results[:5], start=1):
        print(i, "-", r.text)
    driver.quit()


if __name__ == "__main__":
    run()
