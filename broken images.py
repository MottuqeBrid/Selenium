import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://the-internet.herokuapp.com/broken_images"
try:
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get(url)
    images = browser.find_elements(By.TAG_NAME, 'img')
    broken_images = []
    for image in images:
        src = image.get_attribute('src')
        if src:
            res = requests.get(src)
            if res.status_code != 200:
                broken_images.append(src)
                print("Broken Image Found")
    if len(broken_images) > 0:
        print(f"Number of broken images: {len(broken_images)}")
        for broken_image in broken_images:
            print(f"Broken Image: {broken_image}")
    else:
        print("No broken images found")

finally:
    browser.quit()
