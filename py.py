import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/watch?v=tVnN7-RCahY")
time.sleep(5)

try:
    # Find the element with the class name "yt-spec-button-shape-next"
    element = driver.find_element(By.CLASS_NAME, "yt-spec-button-shape-next")
    # Print the value of the element
    print(element.text)
    print("good")

except NoSuchElementException as e:
    print("Element not found:", e)
    print("no")

driver
