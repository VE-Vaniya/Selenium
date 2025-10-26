import sys
from pathlib import Path

# Ensure src folder is on sys.path when running directly from this folder
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from haseeb.driver_setup import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time


def run(query: str = "headphones"):
    driver = get_driver(headless=True)
    try:
        driver.get("https://www.amazon.com/")

        try:
            search = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
            )
        except TimeoutException:
            driver.save_screenshot("open_product_details_no_searchbox.png")
            raise NoSuchElementException("Search box not found; saved screenshot open_product_details_no_searchbox.png")

        search.clear()
        search.send_keys(query)
        try:
            btn = driver.find_element(By.ID, "nav-search-submit-button")
            btn.click()
        except Exception:
            search.submit()

        try:
            first = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div.s-main-slot div[data-component-type='s-search-result'] h2 a"))
            )
            first.click()
        except TimeoutException:
            # fallback attempt
            try:
                first = driver.find_element(By.CSS_SELECTOR, "div[data-component-type='s-search-result'] a.a-link-normal.a-text-normal")
                first.click()
            except Exception as e:
                driver.save_screenshot("open_product_details_no_result.png")
                raise NoSuchElementException("Could not find first search result; saved screenshot open_product_details_no_result.png") from e

        try:
            title = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "productTitle"))
            ).text
        except TimeoutException:
            driver.save_screenshot("open_product_details_no_title.png")
            raise NoSuchElementException("Product title not found; saved screenshot open_product_details_no_title.png")

        price = "n/a"
        try:
            price_el = driver.find_element(By.CSS_SELECTOR, "#priceblock_ourprice, #priceblock_dealprice, #price_inside_buybox")
            price = price_el.text
        except Exception:
            # keep price as n/a or try alternative selectors
            try:
                price = driver.find_element(By.CSS_SELECTOR, ".a-price .a-offscreen").text
            except Exception:
                price = "n/a"

        print("Product title:", title)
        print("Price:", price)
    finally:
        driver.quit()


if __name__ == "__main__":
    run()
