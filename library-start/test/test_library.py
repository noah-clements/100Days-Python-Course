from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import random

URL = 'http://localhost:5000/'

@pytest.fixture(scope="class")
def browser() :
    browser = webdriver.Firefox()
    yield browser
    browser.close()

class TestLibrary():
    def test_home(self, browser):
        browser.get(URL)
        assert "Library" in browser.title
        header_text = browser.find_element(By.TAG_NAME, 'h1').text
        assert "My Library" in header_text

    # @pytest.mark.skip(reason='already added this book. DB requires unique')
    def test_add_new_book(self, browser):
        browser.get(URL + "add")
        assert "Add Book" in browser.title
        browser.find_element(By.NAME, 'title').send_keys('My Antonia')
        browser.find_element(By.NAME, 'author').send_keys('Willa Cather')
        browser.find_element(By.NAME, 'rating').send_keys('6.3')
        browser.find_element(By.CSS_SELECTOR, 'form button').submit()
        WebDriverWait(browser, 10).until(EC.title_is('Library'))
        books = browser.find_elements(By.CSS_SELECTOR, 'ul li')
        added_book = False
        for book in books:
            if 'My Antonia' in book.text:
                added_book = True                
        assert added_book

    def test_change_rating(self, browser):
        browser.get(URL)
        assert "Library" in browser.title
        books = browser.find_elements(By.CSS_SELECTOR, 'ul li')
        # assert 'My Antonia' in [book.text for book in books]
        for book in books:
            if 'My Antonia' in book.text:
                book.find_element(By.LINK_TEXT, "Change Rating").click()
        WebDriverWait(browser, 10).until(EC.title_is('Edit'))
        assert "Edit Book Rating" in browser.find_element(By.TAG_NAME, 'h1').text
        new_rating = random.randint(1,10) + round(random.random(), 2)
        browser.find_element(By.NAME, 'rating').send_keys(new_rating)
        browser.find_element(By.CSS_SELECTOR, 'form button').submit()
        WebDriverWait(browser, 10).until(EC.title_is('Library'))
        books = browser.find_elements(By.CSS_SELECTOR, 'ul li')
        found_rating = False
        for book in books:
            if 'My Antonia' in book.text and str(new_rating) in book.text:
                found_rating = True
        assert found_rating

    def test_delete_book(self, browser):
        browser.get(URL)
        assert "Library" in browser.title
        books = browser.find_elements(By.CSS_SELECTOR, 'ul li')
        # assert 'My Antonia' in [book.text for book in books]
        there_b4_delete = False
        for book in books:
            if 'My Antonia' in book.text:
                there_b4_delete = True
                book.find_element(By.LINK_TEXT, "Delete").click()
        assert there_b4_delete
        WebDriverWait(browser, 3)
        books = browser.find_elements(By.CSS_SELECTOR, 'ul li')
        # assert 'My Antonia' in [book.text for book in books]
        there_after_delete = False
        for book in books:
            if 'My Antonia' in book.text:
                there_after_delete = True
        assert not there_after_delete

        
            

        