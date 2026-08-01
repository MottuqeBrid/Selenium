import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

options = Options()
# options.add_argument("--headless")
# profile
# options.add_argument("-profile")
# options.add_argument(r"C:\Users\YourName\AppData\Roaming\Mozilla\Firefox\Profiles\your_profile_folder")
# options.add_argument(r" C:\Users\USER\AppData\Roaming\Mozilla\Firefox\Profiles\05pbec2l.default-release")

# options.add_argument(r"C:\Users\USER\AppData\Roaming\Mozilla\Firefox\Profiles\05pbec2l.default-release")

import shutil, tempfile


def ignore_lock(dir, files):
    return [f for f in files if f in ("parent.lock", "lock", ".parentlock")]


original = r"C:\Users\USER\AppData\Roaming\Mozilla\Firefox\Profiles\n1lMGCin.Profile 1"
temp_profile = tempfile.mkdtemp()
shutil.copytree(original, temp_profile, dirs_exist_ok=True, ignore=ignore_lock)

options.add_argument("-profile")
options.add_argument(temp_profile)

# Chrome
# # Path to the main "User Data" directory (Do not include the specific profile folder here)
# options.add_argument(r"user-data-dir=C:\Users\YourName\AppData\Local\Google\Chrome\User Data") #
#
# # Name of the specific profile folder you want to use
# options.add_argument("profile-directory=Default") # Use "Profile 1", "Profile 2", etc. if not Default


driver = webdriver.Firefox(options=options)
try:
    driver.maximize_window()
    driver.get("https://selenium.dev")
    driver.switch_to.new_window("tab")
    driver.get("https://playwright.dev/")

    number_of_tabs = len(driver.window_handles)
    print(number_of_tabs)
    tabs_value = driver.window_handles
    print(tabs_value)
    current_tab = driver.current_window_handle
    print(current_tab)
    driver.find_element(By.CSS_SELECTOR, ".getStarted_Sjon").click()
    FirstTab = driver.window_handles[0]
    if current_tab != FirstTab:
        driver.switch_to.window(FirstTab)
        print(FirstTab, "Switch")
    driver.find_element(By.XPATH, "//span[normalize-space()='Downloads']").click()
finally:
    time.sleep(5)
    driver.quit()
    print("Done")
