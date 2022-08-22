import toml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

# from selenium.webdriver.common.keys import Keys
import time
# import pprint

URL = 'https://www.linkedin.com/jobs/search/?currentJobId=3199980111&f_AL=true&f_WT=2&keywords=python%20developer&sortBy=R'

def login():
    signin = driver.find_element(By.LINK_TEXT, 'Sign in')
    signin.click()

    time.sleep(1)
    username = config['LinkedIn']['username']
    pwd = config['LinkedIn']['password']

    driver.find_element(By.CSS_SELECTOR, 'form #username').send_keys(username)
    driver.find_element(By.CSS_SELECTOR, 'form #password').send_keys(pwd)
    driver.find_element(By.CSS_SELECTOR, 'form button').click()


def save_jobs():
    driver.maximize_window()
    # a.job-card-container__link
    job_list = driver.find_elements(By.CSS_SELECTOR, 'ul.jobs-search-results__list li.jobs-search-results__list-item')                   

    # job_list = driver.find_elements(By.CSS_SELECTOR, '.job-card-container--clickable')
    print(f"found {len(job_list)} jobs")

    for job in job_list:
        try:
            company = job.find_element(By.CSS_SELECTOR, 'a.job-card-container__link img')
            print(company.get_attribute('title'))
        except NoSuchElementException:
            print ("skipping over a company title - couldn't find the image")
        # print(job.get_attribute('innerHTML'))
        try:
            # driver.execute_script("arguments[0].click();", job)
            job.click()
        except ElementClickInterceptedException:
            print("caught exception what now?")
            driver.execute_script("scroll(0, 250);")
            job.click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, 'button.jobs-save-button').click()

def get_saved_jobs_batch():
    saved_jobs = driver.find_elements(By.CSS_SELECTOR, 'div.entity-result__actions-overflow-menu-dropdown')
    print(f"{len(saved_jobs)} saved jobs to unsave now in this batch")
    return saved_jobs

def unsave() :
    print("unsaving now . . .")
    driver.get('https://www.linkedin.com/my-items/saved-jobs')

    have_more = True
    while have_more:
        saved_jobs = get_saved_jobs_batch()
        if len(saved_jobs) < 1:
            try:
                previous = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Previous"]')
                print("Because of LinkedIn strangeness when clicking Next, now I click Previous")
                previous.click()
                saved_jobs = get_saved_jobs_batch()
            except NoSuchElementException:
                print("no previous button. Break.")
                break
        for job in saved_jobs:
            job.click()
            time.sleep(1)
            # print(job.get_attribute('innerHTML').strip())
            inner_menu = job.find_element(By.CSS_SELECTOR, 'div.artdeco-dropdown__content-inner')
            # print(inner_menu.get_attribute('innerHTML').strip())
            inner_menu.find_elements(By.CSS_SELECTOR, 'span.image-text-lockup__text')[-1].click()
            time.sleep(1)
        try:
            next = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Next"]')
            print("going to click next now. Wish me luck!")
            next.click()
            time.sleep(1)
            # previous = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Previous"]')
            # print("Because of LinkedIn strangeness when clicking Next, now I click Previous")
            # previous.click()
        except NoSuchElementException:
            print("setting condition to false (same as break).")
            have_more = False
                

config = toml.load('.project_config')
driver_path = config['chrome_driver_path']
chrome_executable = Service(executable_path=driver_path, log_path='NUL')
driver = webdriver.Chrome(service=chrome_executable)
driver.get(URL)

login()
time.sleep(1)
# save_jobs()
unsave()

    
driver.quit()