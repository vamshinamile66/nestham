from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

class GrievancePage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.actions = ActionChains(driver)

    # Locators
    home_create_new_button = (By.XPATH, "/html/body/div/div/div/div/div/div[1]/button")
    new_draft_option = (By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/p[2]")
    draft_textarea = (By.XPATH, "/html/body/div/div/main/div/div[2]/div/div[1]/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div/textarea[1]")
    draft_requestor_number = (By.XPATH, "/html/body/div/div/main/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div/div/div[3]/div/div/div/input")
    draft_requestor_name = (By.XPATH, "/html/body/div/div/main/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div/div/div[4]/div/div/input")
    create_draft_button = (By.XPATH, "/html/body/div/div/main/div/div[2]/div/div[2]/div/button[2]")
    move_to_grievance = (By.XPATH, "/html/body/div/div/main/div/div/div[2]/div[2]/div/div/div[3]/div[2]/div[2]/div[4]/div[1]/div[2]/div/div[1]/div[1]/div/span/div/a")
    department_dropdown = (By.XPATH, "/html/body/div/div/main/div/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/div[1]/div/div/input")
    next_button_template = (By.XPATH, "/html/body/div/div/main/div/div[2]/div/div[3]/div[1]/div/button[2]")

    def click_create_new(self):
        """Click on 'Create New' button."""
        self.wait.until(EC.element_to_be_clickable(self.home_create_new_button)).click()
        time.sleep(4)

    def click_new_draft(self):
        """Click on 'New Draft' option."""
        self.wait.until(EC.element_to_be_clickable(self.new_draft_option)).click()

    def fill_grievance_details(self, grievancedesc, draft_requestor_mobile, draft_requestor_name):
        """Fill grievance details."""
        self.wait.until(EC.presence_of_element_located(self.draft_textarea)).send_keys(grievancedesc)
        self.wait.until(EC.presence_of_element_located(self.draft_requestor_number)).send_keys(draft_requestor_mobile)
        self.wait.until(EC.presence_of_element_located(self.draft_requestor_name)).send_keys(draft_requestor_name)

    def click_create_draft(self):
        """Click on 'Create Draft' button."""
        self.wait.until(EC.element_to_be_clickable(self.create_draft_button)).click()
        time.sleep(10)

   
 
