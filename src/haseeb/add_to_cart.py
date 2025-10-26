import sys
from pathlib import Path

# Ensure the repo `src` folder is on sys.path so absolute imports work when
# running this script directly from inside the `haseeb` folder:
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from haseeb.driver_setup import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time


def run(query: str = "usb flash drive"):
    driver = get_driver(headless=False)
    try:
        driver.get("https://www.amazon.com/")
        # enter search query and submit
        search = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
        )
        search.clear()
        search.send_keys(query)
        # click search button (more reliable than submit)
        try:
            btn = driver.find_element(By.ID, "nav-search-submit-button")
            btn.click()
        except Exception:
            search.send_keys("\n")

        # wait for search results to appear
        try:
            first = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div.s-main-slot div[data-component-type='s-search-result'] h2 a"))
            )
            first.click()
        except TimeoutException:
            # try a broader selector as a fallback
            try:
                first = driver.find_element(By.CSS_SELECTOR, "div[data-component-type='s-search-result'] a.a-link-normal.a-text-normal")
                first.click()
            except Exception as e:
                # save screenshot for debugging and re-raise a helpful message
                driver.save_screenshot("add_to_cart_no_results.png")
                raise NoSuchElementException("Could not find first search result; saved screenshot add_to_cart_no_results.png") from e
        time.sleep(2)
        try:
            add_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "add-to-cart-button"))
            )
            add_btn.click()
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "sw-subtotal")))
            print("Clicked Add to Cart; check cart manually or continue automation to verify")
        except TimeoutException as e:
            print("Add to cart button not found or click timed out; saved screenshot to inspect.")
            driver.save_screenshot("add_to_cart_no_addbtn.png")
            print(e)
    finally:
        driver.quit()


if __name__ == "__main__":
    run()
