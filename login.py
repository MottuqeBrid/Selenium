from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()

username = "standard_user"
password = "secret_sauce"

login_url = "https://www.saucedemo.com"
driver.get(login_url)
username_fild = driver.find_element(By.ID, "user-name")
password_fild = driver.find_element(By.ID, "password")

username_fild.send_keys(username)
password_fild.send_keys(password)

login_btn = driver.find_element(By.ID, "login-button")
assert not login_btn.get_attribute("disabled")
login_btn.click()

success_element = driver.find_element(By.CSS_SELECTOR, ".title")
assert success_element.text == "Products"