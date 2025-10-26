from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def get_driver(headless: bool = True):
    """Return a simple Chrome WebDriver. Keeps options minimal for beginners."""
    options = Options()
    if headless:
        options.add_argument("--headless=new")

    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    # small implicit wait to help minor network delays
    driver.implicitly_wait(5)
    return driver
