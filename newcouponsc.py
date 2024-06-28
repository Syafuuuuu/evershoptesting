from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# # Create a WebDriver instance (e.g., Chrome)
# driver = webdriver.Chrome()

couponCodeValid = "FREESHIPPING2020"
couponDescValid = "Totally 100% free shipping, totally not a scam"
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
        try:
            couponCode.send_keys(code)
            print(f"Insertion of {code} succesful!")
        except Exception as e:
            print(f"Field insertion failed! Error: {e}")
            
        # time.sleep(2)
        try:
            couponDesc.send_keys(desc)
            print(f"Insertion of {desc} succesful!")
        except Exception as e:
            print(f"Field insertion failed! Error: {e}")
               
        # time.sleep(2)
        #couponStatus.click()
        try:
            couponamnt.send_keys(amnt)
            print(f"Insertion of {amnt} succesful!")
        except Exception as e:
            print(f"Field insertion failed! Error: {e}")
        # time.sleep(2)
        #couponBox.click()
        try:
            couponType.click()
        except Exception as e:
            print(f"Field insertion failed! Error: {e}")
            print(f"Selection of coupon type succesful!")
        # time.sleep(2)
        try:
            submit_button.click()
        except Exception as e:
            print(f"Field insertion failed! Error: {e}")
            print(f"Coupon saved succesfully!")
        
        # Check if the "font-bold" element exists (indicating success)
        print(f"Details: Code:{code}, Amount:{amnt}")
        print("Test successful!")
        
        # Take a screenshot and get the filename
        time.sleep(1)
        filename = f"C:/Users/User/Documents/GitHub/Selenium/CouponSS/Coupon_{count}_{code}_{amnt}_{testtype}.png"
        driver.save_screenshot(filename)
        time.sleep(2)
        
        #------------Delete created coupon--------------
        driver.get("http://localhost:3000/admin/coupons")
        time.sleep(2)
        # selectCoupon = driver.find_element(by=By.XPATH, value="//div[@id='app']/div/div[2]/div[2]/div/div[2]/table/tbody/tr[2]/td/div/div/label/span")
        # selectDelete = driver.find_element(by=By.XPATH, value="//div[@id='app']/div/div[2]/div[2]/div/div[2]/table/tbody/tr/td/div/a[4]")
        # confDelete = driver.find_element(by=By.XPATH, value="//body[@id='body']/div[2]/div/div/div/div[3]/div/div/button[2]/span")
        
        try:
            selectCoupon = driver.find_element(by=By.XPATH, value="//div[@id='app']/div/div[2]/div[2]/div/div[2]/table/tbody/tr[2]/td/div/div/label/span")
            selectCoupon.click()
            time.sleep(2)
            selectDelete = driver.find_element(by=By.XPATH, value="//div[@id='app']/div/div[2]/div[2]/div/div[2]/table/tbody/tr/td/div/a[4]")
            selectDelete.click()
            time.sleep(2)
            confDelete = driver.find_element(by=By.XPATH, value="//body[@id='body']/div[2]/div/div/div/div[3]/div/div/button[2]/span")
            confDelete.click()
            time.sleep(2)
        except Exception as e:
            print(f"Field insertion failed! Error: {e}")

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
        
