import toml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import time

URL = 'https://orteil.dashnet.org/cookieclicker/'


config = toml.load('.project_config')
driver_path = config['chrome_driver_path']
chrome_executable = Service(executable_path=driver_path, log_path='NUL')
driver = webdriver.Chrome(service=chrome_executable)
driver.get(URL)

driver.implicitly_wait(time_to_wait=10)
driver.find_element(By.ID, 'langSelect-EN').click()

cookie_btn = driver.find_element(By.CSS_SELECTOR, '#cookieAnchor button')
product_list = driver.find_element(By.ID, 'products')


game_time = time.time() + 60*5
check_time = time.time() + 7
i=0
while True:
    cookie_btn.click()
    now = time.time()
    if now > game_time:
        break
    elif now > check_time:
        # cookies = int(driver.find_element(By.ID, 'cookies').text.rstrip(' cookies'))
        products = product_list.find_elements(By.CSS_SELECTOR, "div.product.unlocked.enabled")
        product = products[-1]
        product_no = product.get_property('id')
        if product_no == 'product0':
            continue
        elif i > 5 and product_no == 'product1':
            continue
        else:
            product.click()
            i += 1
        check_time = now + 7

cookie_numbers = driver.find_element(By.ID, 'cookiesPerSecond')

print(cookie_numbers)
print(cookie_numbers.text)

driver.quit()
