import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/watch?v=tVnN7-RCahY")
time.sleep(10)
# Get all button elements
buttons = driver.find_elements(By.CLASS_NAME, "yt-spec-button")
time.sleep(2)

for value in buttons:
        print(value.text)

# Print classname for each button
# print("Number of buttons:", len(buttons))
# try:
#     with open("button_class_names.txt", "w") as file:
#         for button in buttons:
#             class_name = button.get_attribute("class")
#             print("Classname:", class_name)
#             file.write(class_name + "\n")
#     print("Class names written to 'button_class_names.txt' file.")
        
# except NoSuchElementException as e:
#     print("Element not found:", e)

driver.quit()
