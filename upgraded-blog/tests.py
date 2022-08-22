from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest


class TestUpgradeBlog(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()
        self.url = 'http://localhost:5000/'
        return super().setUp()

    def tearDown(self) -> None:
        self.browser.quit()
        return super().tearDown()

    def test_home_page(self):
        self.browser.get(self.url)
        self.assertIn("Noah's Blog", self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn("Noah's Blog", header_text)

    def test_about_page(self):
        self.browser.get(self.url + '/about')
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn("About Me", header_text)

    def test_contact_page(self):
        self.browser.get(self.url + '/contact')
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn("Contact", header_text)

    def test_submit_contact_form(self):
        self.browser.get(self.url + '/contact')
        self.browser.find_element(By.ID, 'name').send_keys("Noah Clements")
        self.browser.find_element(By.ID, 'email').send_keys('noahclemtest@gmail.com')
        self.browser.find_element(By.ID, 'phone').send_keys('(301) 642-9595')
        self.browser.find_element(By.ID, 'message').send_keys("You look Marvelous!")
        self.browser.find_element(By.CSS_SELECTOR, 'form button').submit()
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.success')))
        print(self.browser.find_element(By.CSS_SELECTOR, 'div.success h1').text)
        self.assertIn("Successfully", self.browser.find_element(By.CSS_SELECTOR, 'div.success h1').text)

    # def test_email_submitted_contact_form(self):
    #     self.test_submit_contact_form()
    #     self.browser.get("https://www.gmail.com")
    #     self.assertIn("Noah Clements", self.browser.find_element(By.CSS_SELECTOR, 'span.bqe').text)

    def test_post_page(self):
        self.browser.get(self.url + '/post/1869')
        header_text = self.browser.find_element(By.TAG_NAME,'h1').text
        self.assertIn("The Barefoot Lawyer Breaks Down", header_text)
        self.assertIn("Noah Clements", self.browser.find_element(By.CSS_SELECTOR, 'span.meta a').text)

if __name__ == '__main__':  
    unittest.main()