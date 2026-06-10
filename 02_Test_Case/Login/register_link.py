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

print("Running TC_LOGIN_010")

driver = create_driver()

driver.get(
    "https://practicesoftwaretesting.com/auth/login"
)

try:
    register_login = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable(
            (By.CSS_SELECTOR, '[data-test="register-link"]')
        )
    )
    
    register_login.click()
    
    WebDriverWait(driver, 10).until(
        lambda d: "https://practicesoftwaretesting.com/auth/register" in d.current_url
    )
    
    print("PASS - TC_LOGIN_010")
    passed += 1
    
except Exception as e:
    print("FAIL - TC_LOGIN_010")
    print(e)
    failed += 1
    
finally:
    driver.quit()
    
print("\n========== TEST SUMMARY ==========")
print("Total  : 1")
print(f"Passed : {passed}")
print(f"Failed : {failed}")
print("===================================")