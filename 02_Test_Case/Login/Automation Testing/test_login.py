import sys
import os

ROOT_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../")
)

sys.path.append(ROOT_DIR)

from utils.driver_setup import create_driver
from data.data_login import test_data
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 

passed = 0
failed = 0

for tc_id, email, password, expected in test_data:
    
    driver = create_driver()
    
    try:
        print(f"Running {tc_id}")
        
        # akses url login
        driver.get(
            "https://practicesoftwaretesting.com/auth/login"
        )
        
        # email
        email_input = WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located(
                (By.ID, "email")
            )
        )
        
        email_input.clear()
        email_input.send_keys(email)
        
        # password
        password_input = driver.find_element(
            By.ID, "password"
        )
        
        password_input.clear()
        password_input.send_keys(password)
        
        # login button
        if tc_id == "TC_LOGIN_013":
            for i in range(5):
                login_button = WebDriverWait(driver, 10).until(
                    ec.element_to_be_clickable(
                        (By.CSS_SELECTOR, '[data-test="login-submit"]')
                    )
                )
                
                login_button.click()
                print(f"Klik Login ke - {i + 1}")
                
            actual = "not-locked"
                
            try:
                locked_message = WebDriverWait(driver, 10).until(
                    ec.visibility_of_element_located(
                        (By.CSS_SELECTOR, '[data-test="login-error"]')
                    )
                )
                
                print("Pesan error:", locked_message.text)
                
                if "locked" in locked_message.text.lower():
                    actual = "locked"
                    
            except:
                    actual = "not-locked"
            
        else:
            login_button = WebDriverWait(driver, 10).until(
                ec.element_to_be_clickable(
                    (By.CSS_SELECTOR, '[data-test="login-submit"]')
                    )
                )

            login_button.click()
        
            # asumsi gagal dulu
            actual = False
            
            try:
                account_title = WebDriverWait(driver, 10).until(
                    ec.visibility_of_element_located(
                        (By.CSS_SELECTOR, '[data-test="page-title"]')
                    )
                )
                
                if "/account" in driver.current_url and account_title.text == "My account":
                    actual = True
                    
            except:
                actual = False
            
        if actual == expected:
            print(f"Pass - {tc_id}")
            passed += 1
        else:
            print(f"Fail - {tc_id}")
            print(f"Expected: {expected}")
            print(f"Actual: {actual}")
            failed += 1
            
    except Exception as e:
        
        print(f"ERROR - {tc_id}")
        print(e)
        
        failed += 1
        
    finally:
        driver.quit()
        
print("\n========== TEST SUMMARY ==========")
print(f"Total  : {len(test_data)}")
print(f"Passed : {passed}")
print(f"Failed : {failed}")
print("===================================")