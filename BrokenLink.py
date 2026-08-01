import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://jquery.com"
# url = "https://openjsf.org/cla/yuy"
try:
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(url)
    all_links = driver.find_elements(By.TAG_NAME, 'a')
    print(f"Total Number of links: {len(all_links)}")

    for link in all_links:
        href: str = link.get_attribute('href')
        res = requests.get(href)
        if res.status_code >= 400:
            print(f"Broken link: {href}\n(Status Code: {res.status_code})")



except Exception as e:
    print(f"Error: {e}")
finally:
    time.sleep(5)
    driver.quit()
