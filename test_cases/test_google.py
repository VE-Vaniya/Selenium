import time

def test_google_title(driver):
    print(f"--- Starting test_google_title on {driver.name} ---")
    driver.get("https://www.google.com")
    print(f"Page title is: {driver.title}")
    assert "Google" in driver.title
    time.sleep(1) # Adding a small pause just so you can see it
    print(f"--- Finished test_google_title on {driver.name} ---")