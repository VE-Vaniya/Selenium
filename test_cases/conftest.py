import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from dotenv import load_dotenv
import os

load_dotenv()
GRID_URL = f"http://{os.getenv('GRID_IP')}:4444/wd/hub"


@pytest.fixture(params=["chrome", "firefox", "edge"])
def driver(request):
    browser = request.param
    print(f"\n[Fixture] Creating {browser} driver...")

    if browser == "chrome":
        options = ChromeOptions()
        wd = webdriver.Remote(command_executor=GRID_URL, options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        wd = webdriver.Remote(command_executor=GRID_URL, options=options)
    elif browser == "edge":
        options = EdgeOptions()
        wd = webdriver.Remote(command_executor=GRID_URL, options=options)
    else:
        raise Exception("Unsupported browser!")

    # Yield the driver to the test function
    yield wd

    # This code runs *after* the test function completes
    print(f"\n[Fixture] Quitting {browser} driver...")
    wd.quit()
