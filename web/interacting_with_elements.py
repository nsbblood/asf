import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)

try:
    driver.get('https://the-internet.herokuapp.com/')

    # Explicitly wait for the link to be present
    form_auth_link = wait.until(
        EC.presence_of_element_located((By.LINK_TEXT, "Form Authentication"))
    )
    form_auth_link.click()  
    time.sleep(3)

    username = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#username'))
    )
    username.send_keys('tomsmith')

    # Find and interact with the password field and submit button
    password = driver.find_element(By.CSS_SELECTOR, '#password')
    password.send_keys('SuperSecretPassword!')
    driver.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()

    # Wait for the logout link to be present and click it
    logout_link = wait.until(
        EC.presence_of_element_located((By.LINK_TEXT, 'Logout'))
    )
    logout_link.click() 

    # Wait for the flash message to be present and assert its text
    flash = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#flash'))
    )
    assert 'logged out' in flash.text.lower()  # Case-insensitive check

finally:
    driver.quit()
