from selenium import webdriver
import time

driver1 = webdriver.Firefox()
driver1.get("https://the-internet.herokuapp.com")

driver2 = webdriver.Firefox()
driver2.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")