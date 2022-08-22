from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()

browser.get("http://localhost:5000")
assert 'Form' in browser.title

browser.find_element(By.NAME, 'name').send_keys('Noah')
browser.find_element(By.NAME, 'pwd').send_keys('bubba1')
browser.find_element(By.CSS_SELECTOR, 'button').click()

assert "Success!" in browser.page_source
assert "bubba1" in browser.page_source
