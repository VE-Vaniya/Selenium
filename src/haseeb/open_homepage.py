import sys
from pathlib import Path
import time
from selenium.webdriver.common.by import By

# Ensure repo src is on sys.path when running directly from this folder
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from haseeb.driver_setup import get_driver


def open_homepage():
    driver = get_driver(headless=False)
    driver.get("https://www.amazon.com/")
    print("Amazon homepage opened.")
    time.sleep(5)  # Keep browser open to view homepage
    driver.quit()


if __name__ == "__main__":
    open_homepage()
