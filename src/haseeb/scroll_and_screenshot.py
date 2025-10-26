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
from selenium.common.exceptions import TimeoutException
import time


def run(query: str = "wireless mouse"):
    driver = get_driver(headless=True)
    try:
        driver.get("https://www.amazon.com/")
        try:
            search = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
            )
        except TimeoutException:
            driver.save_screenshot("scroll_no_searchbox.png")
            print("Search box not found; saved scroll_no_searchbox.png")
            return

        search.clear()
        search.send_keys(query)
        try:
            driver.find_element(By.ID, "nav-search-submit-button").click()
        except Exception:
            search.submit()

        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.s-main-slot div[data-component-type='s-search-result']"))
            )
        except TimeoutException:
            driver.save_screenshot("scroll_no_results.png")
            print("No search results; saved scroll_no_results.png")
            return

        # scroll down gradually
        for y in range(0, 2000, 400):
            driver.execute_script(f"window.scrollTo(0, {y});")
            time.sleep(0.5)
        path = "amazon_search_scroll.png"
        driver.save_screenshot(path)
        print("Saved screenshot to", path)
    finally:
        driver.quit()


if __name__ == "__main__":
    run()
