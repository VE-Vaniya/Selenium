import time

def test_python_title(driver):
    """
    This test ALSO uses the 'driver' fixture.
    Just like the Google test, this function will ALSO run TWICE:
    1. Once with the Chrome driver
    2. Once with the Firefox driver
    """
    print(f"--- Starting test_python_title on {driver.name} ---")
    driver.get("https://www.python.org")
    print(f"Page title is: {driver.title}")
    assert "Python" in driver.title
    time.sleep(1) # Adding a small pause
    print(f"--- Finished test_python_title on {driver.name} ---")