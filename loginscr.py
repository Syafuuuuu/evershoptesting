from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from os import path
import time

# # Create a WebDriver instance (e.g., Chrome)
# driver = webdriver.Chrome()

email_array = ["admin@admin.com","admin@d.com","admin"," "]
password_array = ["SKIW3113", "skiw3113", " "]

def LoginTest(em, pas, count, testtype):
    # Create a WebDriver instance (e.g., Chrome)
    driver = webdriver.Chrome()
    try:
        # Navigate to the login page
        driver.get("http://localhost:3000/admin/login")

        # Find login elements
        login = driver.find_element(by=By.NAME, value="email")
        password = driver.find_element(by=By.NAME, value="password")
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

        # Enter login credentials and submit
        login.send_keys(em)
        password.send_keys(pas)
        submit_button.click()

        # Wait for the page to load
        # driver.implicitly_wait(20.0)
        time.sleep(2) # take a pause 10 seconds

        # Check if the "font-bold" element exists (indicating success)
        message = driver.find_element(by=By.CLASS_NAME, value="font-bold")
        text = message.text
        print(f"Details: Email:{em}, Pass:{pas}, Target Text: {message}")
        print(f"Test successful! Message: {text}")
        
        # Take a screenshot and get the filename
        filename = f"C:/Users/User/Documents/GitHub/Selenium/LoginSS/Login_{count}_{em}_{pas}_{testtype}.png"
        driver.save_screenshot(filename)

        
        

    except Exception as e:
        print(f"Test failed! Error: {e}")

    finally:
        # Clean up and quit the WebDriver
        driver.quit()

print("Email testing")
for c, email in enumerate(email_array):
    LoginTest(email, "SKIW3113", c, "EmailTest")

print("Password testing")
for c, password in enumerate(password_array):
    LoginTest("admin@admin.com", password, c, "PassTest")
        

    
    
