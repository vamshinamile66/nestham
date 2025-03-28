from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Waits up to 10 seconds
  
    # Locators     
    username_input = (By.ID, "username") 
    password_input = (By.ID, "password")
    login_button = (By.XPATH, "//button[@type='submit']")
    alert_message = (By.CSS_SELECTOR, ".MuiAlert-message")

    # Login method
    def login(self, username, password):
        self.wait.until(EC.visibility_of_element_located(self.username_input)).send_keys(username)
        self.wait.until(EC.visibility_of_element_located(self.password_input)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()

        print("Login successful, waiting for alert...")

        try:
            # Wait for alert to appear
            alert = self.wait.until(EC.presence_of_element_located(self.alert_message))
            alert_text = alert.text.strip()

            if alert_text:
                print("Alert Message:", alert_text)
            else:
                print("Alert is present but contains no text.")
        except:
            print("No alert message appeared.")
