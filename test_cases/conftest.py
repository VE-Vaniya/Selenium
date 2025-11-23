import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

# !!! IMPORTANT: Make sure this IP address is correct for your Grid Hub !!!
GRID_URL = "http://192.168.18.38:4444/wd/hub"

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    """
    This fixture is the core of the setup.
    It's parameterized with "chrome" and "firefox".
    Any test that uses this 'driver' fixture will
    automatically run TWICE: once for each parameter.
    """
    browser = request.param
    print(f"\n[Fixture] Creating {browser} driver...")

    if browser == "chrome":
        options = ChromeOptions()
        # options.add_argument("--headless")  # You can uncomment this later if you don't want to see the browser
        wd = webdriver.Remote(command_executor=GRID_URL, options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        # options.add_argument("--headless")  # You can uncomment this later
        wd = webdriver.Remote(command_executor=GRID_URL, options=options)

    else:
        raise Exception("Unsupported browser!")

    # Yield the driver to the test function
    yield wd
    
    # This code runs *after* the test function completes
    print(f"\n[Fixture] Quitting {browser} driver...")
    wd.quit()