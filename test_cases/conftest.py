import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

# !!! IMPORTANT: Make sure this IP address is correct for your Grid Hub !!!
GRID_URL = "http://172.23.16.1:4444/wd/hub"

@pytest.fixture(params=["chrome", "firefox", "edge"])
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