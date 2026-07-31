import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://www.google.com")

viewports = [(1024, 768), (768, 1024), (375, 667), (414, 896)]

try:
    for width, height in viewports:
        driver.set_window_size(width, height)
        time.sleep(3)
finally:
    driver.quit()
