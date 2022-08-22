import toml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

config = toml.load('.project_config')
driver_path = config['chrome_driver_path']

chrome_executable = Service(executable_path=driver_path, log_path='NUL')

driver = webdriver.Chrome(service=chrome_executable)

# driver.get('https://smile.amazon.com/Instant-Pot-Pressure-Steamer-Sterilizer/dp/B08PQ2KWHS/ref=dp_fod_1?pd_rd_i=B08PQ2KWHS&psc=1')
# price = driver.find_element(By.CLASS_NAME, 'a-offscreen')
# print (f"Check {price.tag_name}")
# print(price.get_attribute('innerHTML'))

driver.get('https://www.python.org')
# event_blk = driver.find_element(By.CLASS_NAME, 'event-widget')
# events = event_blk.find_elements(By.TAG_NAME, 'li')
# events_dict = {}
# i = 0
# for event in events:
#     time = event.find_element(By.TAG_NAME, 'time').text
#     name = event.find_element(By.TAG_NAME, 'a').get_attribute('innerHTML')
#     events_dict[i] = {'time': time, 'name': name}
#     i += 1
#     # print(event.get_attribute('innerHTML'))

# looks like the class solution was much more elegant 
# if for no other reason that it doesn't have to find in a loop
event_times = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
event_names = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')

# comprehension in this case doesn't seem much different than using for loop
events_dict = {
    i: {
        'time': event_times[i].text,
        'name': event_names[i].text
    }
    for i in range(len(event_names)) 
}
# for i in range(len(event_times)):
#     events_dict[i] = {
#         'time': event_times[i].text,
#         'name': event_names[i].text
#         }

print(events_dict)

# driver.close()
driver.quit()
