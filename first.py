from selenium import webdriver

browser = webdriver.Firefox()
browser.get("https://selenium.dev")
browser.maximize_window()
title = browser.title
print(title)

assert  "Selenium" in title
