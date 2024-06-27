from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# # Create a WebDriver instance (e.g., Chrome)
# driver = webdriver.Chrome()

couponCodeValid = "FREESHIPPING2020"
couponDescValid = "Tottally 100% free shipping, totally not a scam"
couponAmntValid = "100"

couponCodeArray = [couponCodeValid, "", "", "", ""]
couponDescArray = [couponDescValid, ""]
couponAmntArray = [couponAmntValid, ""]


def NewCouponTest(code, desc, amnt, count, testtype):
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
        login.send_keys("admin@admin.com")
        password.send_keys("SKIW3113")
        submit_button.click()

        # Wait for the page to load
        # driver.implicitly_wait(20.0)
        time.sleep(2) # take a pause 10 seconds
        
        # newCoupon = driver.find_element(by=By.XPATH, value="")
        # newCoupon.click()
        driver.get("http://localhost:3000/admin/coupon/new")
        time.sleep(1)
        
        
        #----- Start Coupon testing ------
        #Get fields
        couponCode = driver.find_element(by=By.NAME, value="coupon")
        couponDesc = driver.find_element(by=By.ID, value="description")
        #couponStatus = driver.find_element(by=By.CLASS_NAME, value="toggle enabled")
        couponamnt = driver.find_element(by=By.NAME, value="discount_amount")
        #couponBox = driver.find_element(by=By.ID, value="free_shipping")
        submit_button = driver.find_element(by=By.XPATH, value="//form[@id='couponForm']/div[2]/button[2]/span")
        couponType = driver.find_element(by=By.XPATH, value="//form[@id='couponForm']/div/div[2]/div[2]/div/div/div/div/div/div/div/label/span")
        
        # Insert values
        couponCode.send_keys(code)
        time.sleep(2)
        couponDesc.send_keys(desc)
        time.sleep(2)
        #couponStatus.click()
        couponamnt.send_keys(amnt)
        time.sleep(2)
        #couponBox.click()
        couponType.click()
        time.sleep(2)
        submit_button.click()
        
        # Check if the "font-bold" element exists (indicating success)
        print(f"Details: Code:{code}, Amount:{amnt}")
        print("Test successful!")
        
        # Take a screenshot and get the filename
        time.sleep(1)
        filename = f"C:/Users/User/Documents/GitHub/Selenium/CouponSS/Coupon_{count}_{code}_{amnt}_{testtype}.png"
        driver.save_screenshot(filename)

    except Exception as e:
        print(f"Test failed! Error: {e}")

    finally:
        # Clean up and quit the WebDriver
        driver.quit()

print("Coupon testing")
NewCouponTest(couponCodeValid, couponDescValid, couponAmntValid, 1, "CouponTest")
# for c, password in enumerate(password_array):
#     LoginTest("admin@admin.com", password, c, "PassTest")

# print("Email testing")
# for c, email in enumerate(email_array):
#     LoginTest(email, "SKIW3113", c, "EmailTest")

# print("Password testing")
# for c, password in enumerate(password_array):
#     LoginTest("admin@admin.com", password, c, "PassTest")
        

    
    
