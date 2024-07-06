import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()

try:
    driver.get('https://www.youtube.com')
    time.sleep(5)


finally:
    driver.quit()