from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

URL = 'http://localhost:5000/'

class TestCafeSite(unittest.TestCase):
    browser: webdriver.Firefox = None
    
    @classmethod
    def setUpClass(cls) -> None:
        cls.browser = webdriver.Firefox()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.browser.quit()
        

    def test_home_page(self):
        self.browser.get(URL)
        self.assertIn("Coffee", self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn("Coffee & Wifi", header_text)

    def test_home_button(self):
        self.browser.get(URL)
        self.browser.find_element(By.CSS_SELECTOR, 'a.btn').click()
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
        self.assertIn("Coffee & Wifi", self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn("All Cafes", header_text)

    def test_cafe_links(self):
        self.browser.get(f"{URL}/cafes")
        links = self.browser.find_elements(By.CSS_SELECTOR, "table tbody a")
        map_links = [link.get_attribute("href") for link in links]
        for link in map_links:
            print(link)
            self.browser.get(link)
            self.assertIn("Google Maps", self.browser.title)
            self.browser.back()

    def test_cafe_add(self):
        self.browser.get(f"{URL}/add")
        self.browser.find_element(By.NAME, "cafe").send_keys("Caffe Driade")
        self.browser.find_element(By.NAME, "location").send_keys("https://goo.gl/maps/JiQ6T52g4xYSmtw49")
        self.browser.find_element(By.NAME, "open").send_keys("8AM")  
        self.browser.find_element(By.NAME, "close").send_keys("8PM")
        self.browser.find_element(By.NAME, "coffee").send_keys("☕☕☕☕️")
        self.browser.find_element(By.NAME, "wifi").send_keys("💪💪💪")
        self.browser.find_element(By.NAME, "power").send_keys("🔌")
        self.browser.find_element(By.CSS_SELECTOR, 'input.btn').click()
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
        self.assertIn("Coffee & Wifi", self.browser.title)
        self.assertIn("Caffe Driade", self.browser.find_elements(By.CSS_SELECTOR, 'tbody tr')[-1].text)
            



if __name__ == '__main__':  
    unittest.main()