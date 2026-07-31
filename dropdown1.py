import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.maximize_window()
login_url = "https://the-internet.herokuapp.com/dropdown"

driver.get(login_url)

dropdown_element = driver.find_element(By.ID, "dropdown")
select = Select(dropdown_element)
# Select the value by visible text
# Select tge value by value
# Select tge option by using a value

# select.select_by_visible_text("Option 1")
# time.sleep(3)
# select.select_by_index(2)
# time.sleep(3)
# select.select_by_value("1")

# count value
option_count = len(select.options)
print(option_count)

target_value = "Option 3"

for option in select.options:
    if option.text == target_value:
        option.click()
        print(f"Selected option: {option.text}")
        break
    else:
        print(f"Selected option not found: {target_value}")

time.sleep(3)
driver.close()
