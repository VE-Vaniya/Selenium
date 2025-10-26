import sys
from pathlib import Path

# Ensure src folder is on sys.path when running directly from this folder
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from haseeb.driver_setup import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


def run(query: str = "laptop"):
    driver = get_driver(headless=True)
    try:
        driver.get("https://www.amazon.com/")
        try:
            search = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
            )
        except TimeoutException:
            driver.save_screenshot("search_product_no_searchbox.png")
            print("Search box not found; saved screenshot search_product_no_searchbox.png")
            return

        search.clear()
        search.send_keys(query)
        # click explicit search button when available
        try:
            btn = driver.find_element(By.ID, "nav-search-submit-button")
            btn.click()
        except Exception:
            search.send_keys(Keys.ENTER)

        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.s-main-slot div[data-component-type='s-search-result']"))
            )
        except TimeoutException:
            driver.save_screenshot("search_product_no_results.png")
            print("No search results found; saved screenshot search_product_no_results.png")
            return

        results = driver.find_elements(By.CSS_SELECTOR, "div.s-main-slot div[data-component-type='s-search-result'] h2 a span")
        print(f"Search results for '{query}':")
        if not results:
            print("No result title elements found; saved screenshot for debugging.")
            driver.save_screenshot("search_product_results_empty.png")
            return
        for i, r in enumerate(results[:10], start=1):
            print(i, "-", r.text)
    finally:
        driver.quit()


if __name__ == "__main__":
    run()
