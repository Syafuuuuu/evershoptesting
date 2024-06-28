from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# # Create a WebDriver instance (e.g., Chrome)
# driver = webdriver.Chrome()

couponCodeValid = "FREESHIPPING2020"
couponDescValid = "Totally 100% free shipping, totally not a scam"
couponAmntValid = "100"

couponCodeArray = [couponCodeValid, " ", "@#$%"]
couponDescArray = [couponDescValid, " ", "id=1; SELECT pg_sleep(10);-- -"]
couponAmntArray = [couponAmntValid, "-100", "abc", "^*&", " "]


def NewProductTest(name, sku, price, weight, para, url, qty, count, testtype):
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
        driver.get("http://localhost:3000/admin/products/new")
        time.sleep(1)
        
        
        #----- Start Coupon testing ------
        #Get fields
        prodName = driver.find_element(by=By.NAME, value="name")   
        prodSKU = driver.find_element(by=By.NAME, value="sku")
        prodPrice = driver.find_element(by=By.NAME, value="price")
        prodWeight = driver.find_element(by=By.NAME, value="weight")
        prodDesc = driver.find_element(by=By.XPATH, value="//form[@id='productForm']/div/div/div/div[2]/div/div/div[5]/div[3]/div[2]/div")
        #prodMedia = driver.find_element(by=By.XPATH, value="//div[@id='images']/div/div[2]/input")
        prodURL = driver.find_element(by=By.NAME, value="url_key")
        prodQty = driver.find_element(by=By.NAME, value="qty")
        
        # Insert values
        try:
            prodName.send_keys(name)
            print(f"Insertion of {name} succesful!")
        except Exception as e:
            print(f"Field insertion failed! Error: {e}")
            
        time.sleep(2)
        try:
            prodSKU.send_keys(sku)
            print(f"Insertion of {sku} succesful!")
        except Exception as e:
            print(f"Field insertion failed! Error: {e}")
               
        time.sleep(2)
        #couponStatus.click()
        try:
            prodPrice.send_keys(price)
            print(f"Insertion of {price} succesful!")
        except Exception as e:
            print(f"Field insertion failed! Error: {e}")
            
        time.sleep(2)
        try:
            prodWeight.send_keys(weight)
            print(f"Insertion of {weight} succesful!")
        except Exception as e:
            print(f"Field insertion failed! Error: {e}")
        
        time.sleep(2)    
        try:
            prodDesc.send_keys(para)
            print(f"Insertion of {para} succesful!")
        except Exception as e:
            print(f"Field insertion failed! Error: {e}")
        
        time.sleep(2)    
        try:
            prodQty.send_keys(qty)
            print(f"Insertion of {qty} succesful!")
        except Exception as e:
            print(f"Field insertion failed! Error: {e}")
        
        time.sleep(2)    
        try:
            prodURL.send_keys(url)
            print(f"Insertion of {url} succesful!")
        except Exception as e:
            print(f"Field insertion failed! Error: {e}")
        
        time.sleep(2)    
        try:
            #prodMedia.click()
            time.sleep(3)
            uploadPic = driver.find_element(by=By.XPATH, value="//div[@id='images']/div/div[2]/input")
            uploadPic.send_keys("C:/Users/User/Documents/GitHub/Selenium/LoginSS/Login_0_admin@admin.com_SKIW3113_EmailTest.png")
            
        except Exception as e:
            print(f"Field insertion failed! Error: {e}")
            print(f"Coupon saved succesfully!")
            
        #--Save--
        saveBtn = driver.find_element(by=By.XPATH, value="//form[@id='productForm']/div[2]/button[2]/span")
        saveBtn.click()
        
        # Check if the "font-bold" element exists (indicating success)
        # print(f"Details: Code:{code}, Amount:{amnt}")
        print("Test successful!")
        
        # Take a screenshot and get the filename
        time.sleep(1)
        filename = f"C:/Users/User/Documents/GitHub/Selenium/ProdSS/{testtype}_{count}.png"
        driver.save_screenshot(filename)
        time.sleep(2)
        
        #------------Delete created coupon--------------
        driver.get("http://localhost:3000/admin/products")
        time.sleep(2)
        
        try:
            selectProd = driver.find_element(by=By.XPATH, value="//div[@id='app']/div/div[2]/div[2]/div/div[2]/table/tbody/tr[2]/td/div/div/label/span")
            selectProd.click()
            time.sleep(2)
            selectProd = driver.find_element(by=By.XPATH, value="//div[@id='app']/div/div[2]/div[2]/div/div[2]/table/tbody/tr/td/div/a[4]")
            selectProd.click()
            time.sleep(2)
            confDelete = driver.find_element(by=By.XPATH, value="//body[@id='body']/div[2]/div/div/div/div[3]/div/div/button[2]/span")
            confDelete.click()
            time.sleep(2)
        except Exception as e:
            print(f"Coupon not created!")

    except Exception as e:
        print(f"Test failed! Error: {e}")

    finally:
        # Clean up and quit the WebDriver
        driver.quit()

print("Coupon testing")

NewProductTest("Nike Revolution 4","NJC400","200","4.9","DADASDAS","nike-revolution-4.com","10","1","NewProd")
