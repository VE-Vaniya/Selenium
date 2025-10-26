# simple data scraping example using Selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("http://books.toscrape.com/")

books = driver.find_elements(By.CLASS_NAME, "product_pod")

for book in books:
    title = book.find_element(By.TAG_NAME, "h3").text
    price = book.find_element(By.CLASS_NAME, "price_color").text
    print("Title:", title)
    print("Price:", price)

time.sleep(2)
driver.quit()