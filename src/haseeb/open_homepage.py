import sys
from pathlib import Path

# Ensure src folder is on sys.path when running directly from this folder
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from haseeb.driver_setup import get_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


def run():
    driver = get_driver(headless=True)
    try:
        driver.get("https://www.amazon.com/")
        try:
            # wait for search box or title to indicate page loaded
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
            )
        except TimeoutException:
            # fallback: wait for title to contain 'Amazon' as a looser signal
            try:
                WebDriverWait(driver, 5).until(EC.title_contains("Amazon"))
            except TimeoutException:
                driver.save_screenshot("open_homepage_load_failed.png")
                print("Homepage did not load as expected; saved screenshot open_homepage_load_failed.png")
                return

        print("Title:", driver.title)
    finally:
        driver.quit()


if __name__ == "__main__":
    run()
