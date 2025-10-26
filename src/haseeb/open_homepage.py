import sys
from pathlib import Path

# Ensure src folder is on sys.path when running directly from this folder
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from .driver_setup import get_driver


def run():
    driver = get_driver(headless=True)
    driver.get("https://www.amazon.com/")
    print("Title:", driver.title)
    driver.quit()


if __name__ == "__main__":
    run()
