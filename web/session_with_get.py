import time
from selenium import webdriver

driver=webdriver.Firefox()
try:
    driver.get('https://the-internet.herokuapp.com/')
    time.sleep(3)
finally:
    driver.quit()

