import time

def test_python_title(driver):
    print(f"--- Starting test_python_title on {driver.name} ---")
    driver.get("https://www.python.org")
    print(f"Page title is: {driver.title}")
    assert "Python" in driver.title
    time.sleep(1) # Adding a small pause
    print(f"--- Finished test_python_title on {driver.name} ---")