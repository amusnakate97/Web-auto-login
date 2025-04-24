from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Replace these with your Amazon login credentials
AMAZON_EMAIL = "XXXX"
AMAZON_PASSWORD = "YYYY"

# Initialize the WebDriver (Make sure to download the correct WebDriver for your browser)
driver = webdriver.Chrome()  # Or use webdriver.Firefox(), webdriver.Edge(), etc.

try:
    # Open Amazon login page
    driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
    # Wait for the email input field to be visible and enter the email
    email_field = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.ID, "ap_email"))
    )
    email_field.send_keys(AMAZON_EMAIL)

    # Click the continue button
    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()
    
    time.sleep(5)

    # # Wait for the password input field to be visible and enter the password
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ap_password"))
    )
    password_field.send_keys(AMAZON_PASSWORD)
    
    # # Click the sign-in button
    sign_in_button = driver.find_element(By.ID, "signInSubmit")
    sign_in_button.click()

    # # Wait for a few seconds to ensure login is successful
    time.sleep(100)

    # # Check if login was successful by looking for a specific element (e.g., account name)
    # try:
    #     account_element = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.ID, "nav-link-accountList"))
    #     )
    #     print("Login successful!")
    # except:
    #     print("Login failed. Please check your credentials or the page structure.")
    print("Entered Email")

finally:
    # Close the browser
    driver.quit()