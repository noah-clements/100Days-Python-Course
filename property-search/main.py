import toml
from bs4 import BeautifulSoup
import requests
import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.keys import Keys

config = toml.load('.project_config')

class Property():
    def __init__(self, address:str, price:str, url:str) -> None:
        self.address = address
        self.price = price
        self.url = url

    def __str__(self) -> str:
        return f"house for sale at {self.address} for {self.price}. See {self.url}"

    def __repr__(self) -> str:
        return "Property(address=%r, price=%r, url=%r)" % (self.address, self.price, self.url)
        

def get_properties() -> list[Property]:
    global config
    search_url = config['Zillow']['search-url']

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15",
        "Accept-Language": "en-US"
    }

    resp = requests.get(search_url, headers=headers)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, 'html.parser')
    # print(soup.prettify())
    results = soup.find('ul', class_='photo-cards')
    # print(results.prettify())
    addresses = results.find_all('address', attrs={'data-test':'property-card-addr'})
    addresses = [address.text.strip() for address in addresses]
    # print(addresses)
    links = results.find_all('a', attrs={'data-test':'property-card-link',
                                         'tabindex':'0'})
    links = [link['href'] for link in links]
    print(f"there are {len(links)} links: {links}")
    prices = soup.find_all('span', attrs={'data-test':'property-card-price'})
    # print(prices)
    prices = [price.text for price in prices]
    # print(prices)

    properties = list(zip(addresses, prices, links))
    # print(properties)
    properties = [Property(*property) for property in properties]
    # print(properties)
    return properties
    # print(soup.prettify())

# Google form
def save_properties(properties:list[Property]):
    global config
    driver_path = config['Selenium']['chrome_driver_path']
    form_url = config['Google']['form-url']

    chrome_executable = Service(executable_path=driver_path, log_path='NUL')
    driver = webdriver.Chrome(service=chrome_executable)

    for property in properties:
        driver.get(form_url)
        # print(driver.current_url)
        time.sleep(2)
        
        inputs = driver.find_elements(By.CSS_SELECTOR, 'input[type="text"]')
        # print(len(inputs))
        # inputs = form.find_elements(By.TAG_NAME, 'input')
        inputs[0].send_keys(property.address)
        inputs[1].send_keys(property.price)
        inputs[2].send_keys(property.url)
        driver.find_element(By.CSS_SELECTOR, 'div[role="button"]').click()

    driver.quit()

properties = get_properties()
# print(properties)
save_properties(properties)
print("done")