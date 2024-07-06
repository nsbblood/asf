from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #make your code better

driver=webdriver.Firefox()

try:
    wait= WebDriverWait(driver,10)
    driver.get('https://the-internet.herokuapp.com/')

    wait.until(EC.presence_of_all_elements_located(
        (By.LINK_TEXT, 'Form Authentication')
    ))
   
    wait.until(EC.url_to_be('https://the-internet.herokuapp.com/'))
finally:
    driver.quit()