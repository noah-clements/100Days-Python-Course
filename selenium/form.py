import toml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = 'https://secure-retreat-92358.herokuapp.com/'

config = toml.load('.project_config')
driver_path = config['chrome_driver_path']
chrome_executable = Service(executable_path=driver_path, log_path='NUL')
driver = webdriver.Chrome(service=chrome_executable)
driver.get(URL)

driver.find_element(By.NAME, 'fName').send_keys('Noah')
driver.find_element(By.NAME, 'lName').send_keys('Clements')
driver.find_element(By.NAME, 'email').send_keys('noahclements@gmail.com')
driver.find_element(By.CSS_SELECTOR, 'button').click()



