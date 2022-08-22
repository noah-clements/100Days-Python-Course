import toml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

config = toml.load('.project_config')
driver_path = config['chrome_driver_path']
chrome_executable = Service(executable_path=driver_path, log_path='NUL')
driver = webdriver.Chrome(service=chrome_executable)

driver.get('https://en.wikipedia.org/wiki/Main_Page')

count = driver.find_element(By.CSS_SELECTOR, '#articlecount a[title="Special:Statistics"]')
# count.click()
print(count.text)

search = driver.find_element(By.NAME, 'search')
search.send_keys('Python')
search.send_keys(Keys.ENTER)

driver.quit()