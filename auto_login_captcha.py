import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytesseract
from PIL import Image

# Replace these with your login credentials
EMAIL = "XXXX"
PASSWORD = "XXXX"

# Initialize the WebDriver (Make sure to download the correct WebDriver for your browser)
driver = webdriver.Chrome()  # Or use webdriver.Firefox(), webdriver.Edge(), etc.

try:
    # Open the login page
    driver.get("https://atlasauth.b2clogin.com/f50ebcfb-eadd-41d8-9099-a7049d073f5c/b2c_1a_atoproduction_atlas_susi/oauth2/v2.0/authorize?client_id=607d08d6-b63b-4735-ad82-05dfcff7efa4&redirect_uri=https%3A%2F%2Fwww.usvisascheduling.com%2Fsignin-aad-b2c_1&response_type=code%20id_token&scope=openid&state=OpenIdConnect.AuthenticationProperties%3DeydPq_WhfkC5w3l6n-H3wFu2H3UPp4R6cMNplom1r68xPkPeqO9Wt7-79O6b6RSppKnmpdWVh66VtKnNuRs4M_nfm9tk2mtgmY0OFWCwkFUlNTeylc-jFGuCVYti0K2bX2PS-EGF1BJJjSXKTsbP7xFfHwA51MVUTrGRkXx0gH")
     
    time.sleep(5)
    #  # Wait for the checkbox to be visible and click on it
    # checkbox = WebDriverWait(driver, 50).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='checkbox']"))  # Adjust selector if needed
    # )
    # checkbox.click()

    # Wait for the email input field to be visible and enter the email
    email_field = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.ID, "signInName"))  # Replace with the actual ID or selector for the email field
    )
    email_field.send_keys(EMAIL)

    # Wait for the password input field to be visible and enter the password
    password_field = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.ID, "password"))  # Replace with the actual ID or selector for the password field
    )
    password_field.send_keys(PASSWORD)

    time.sleep(10)

    # # Wait for the CAPTCHA image to load
    # captcha_image = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.ID, "captchaImage"))  # Adjust selector for the CAPTCHA image
    # )

    # # Get the CAPTCHA image source URL
    # captcha_src = captcha_image.get_attribute("src")

    # # Download the CAPTCHA image
    # captcha_response = requests.get(captcha_src, stream=True)
    # captcha_file = "captcha.png"
    # with open(captcha_file, "wb") as file:
    #     file.write(captcha_response.content)

    # # Use pytesseract to extract text from the CAPTCHA image
    # captcha_text = pytesseract.image_to_string(Image.open(captcha_file)).strip()
    # print(f"Extracted CAPTCHA text: {captcha_text}")

    # time.sleep(5)

    # # Enter the CAPTCHA text into the CAPTCHA input field
    # captcha_field = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.ID, "captcha"))  # Replace with the actual ID or selector for the CAPTCHA input field
    # )
    # captcha_field.send_keys(captcha_text)

    # # Click the login button
    # login_button = driver.find_element(By.ID, "btnLogin")  # Replace with the actual ID or selector for the login button
    # login_button.click()

    # # Check if login was successful by looking for a specific element (e.g., dashboard or account name)
    # try:
    #     dashboard_element = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.ID, "dashboard"))  # Replace with an element that appears after login
    #     )
    #     print("Login successful!")
    # except:
    #     print("Login failed. Please check your credentials or the page structure.")

finally:
    # Close the browser
    driver.quit()