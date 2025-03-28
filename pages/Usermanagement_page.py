 
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UserManagementPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # Locators
    USER_MANAGEMENT_TAB = (By.XPATH, "//div[5]/ul/li/a/div/div")
    CREATE_USER_BUTTON = (By.XPATH, "//button[contains(text(),'Create New User')]")
    USERNAME_INPUT = (By.XPATH, "//input[@placeholder='Enter your username']")
    MOBILE_INPUT = (By.XPATH, "//input[@placeholder='Enter Mobile Number']")
    EMAIL_INPUT = (By.XPATH, "//input[@placeholder='Enter Email Here']")
    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Enter Password Here']")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(),'Submit')]")
    DELETE_ICON = (By.XPATH, "//button[@title='Delete']")
    CONFIRM_DELETE_BUTTON = (By.XPATH, "/html/body/div[2]/div[3]/div/div[2]/div/div/div/button")

    # Methods
    def navigate_to_usermanagement(self):
        self.wait.until(EC.element_to_be_clickable(self.USER_MANAGEMENT_TAB)).click()

    def create_new_user(self, username, mobile, email, password):
        self.wait.until(EC.element_to_be_clickable(self.CREATE_USER_BUTTON)).click()
        self.wait.until(EC.presence_of_element_located(self.USERNAME_INPUT)).send_keys(username)
        self.wait.until(EC.presence_of_element_located(self.MOBILE_INPUT)).send_keys(mobile)
        self.wait.until(EC.presence_of_element_located(self.EMAIL_INPUT)).send_keys(email)
        self.wait.until(EC.presence_of_element_located(self.PASSWORD_INPUT)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()

    def delete_user(self):
        time.sleep(3)
        self.wait.until(EC.element_to_be_clickable(self.DELETE_ICON)).click()
        self.wait.until(EC.element_to_be_clickable(self.CONFIRM_DELETE_BUTTON)).click()
