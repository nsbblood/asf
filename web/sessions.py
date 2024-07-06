from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

webdriver_path='/Users/enesarikan/desktop/prg/bin'

service = ChromeService(executable_path=webdriver_path)

# Create a Chrome WebDriver instance
driver = webdriver.Chrome(service=service)

# Rest of your code to interact with the browser...

driver.quit()
