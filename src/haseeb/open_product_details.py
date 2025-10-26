import sys
from pathlib import Path

# Ensure src folder is on sys.path when running directly from this folder
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from .driver_setup import get_driver
from selenium.webdriver.common.by import By
import time


def run(query: str = "headphones"):
    driver = get_driver(headless=True)
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
    title = driver.find_element(By.ID, "productTitle").text
    price = "n/a"
    price_elems = driver.find_elements(By.CSS_SELECTOR, "#priceblock_ourprice, #priceblock_dealprice, #price_inside_buybox, .a-price .a-offscreen")
    if price_elems:
        price = price_elems[0].text
    print("Product title:", title)
    print("Price:", price)
    driver.quit()


if __name__ == "__main__":
    run()
