import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
# url = "https://opensource-demo.orangehrmlive.com"
url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
driver.get(url)
# driver.minimize_window()
# driver.fullscreen_window()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, ".oxd-text.oxd-text--p.orangehrm-login-forgot-header").click()
time.sleep(5)
driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)
driver.refresh()
time.sleep(5)
driver.quit()
