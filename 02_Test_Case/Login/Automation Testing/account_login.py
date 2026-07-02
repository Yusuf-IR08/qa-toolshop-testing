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

print("Running TC_LOGIN_007")

driver = create_driver()

driver.get(
    "https://practicesoftwaretesting.com/auth/login"
)

try:
    google_login = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable(
            (By.CLASS_NAME, "google-sign-in-button")
        )
    )
    
    google_login.click()
    
    WebDriverWait(driver, 10).until(
        lambda d: len(d.window_handles) > 1 or "account.google.com" in d.current_url
    )
    
    print("Pass - TC_LOGIN_007")
    passed += 1
    
except Exception as e:
    print("Fail - TC_LOGIN_007")
    print(e)
    failed += 1

finally:
    driver.quit()
    
print("\n========== TEST SUMMARY ==========")
print("Total  : 1")
print(f"Passed : {passed}")
print(f"Failed : {failed}")
print("===================================")