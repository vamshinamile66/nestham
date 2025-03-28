from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

class DevelopmentPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def navigate_to_development_tab(self):
        development_module_tab = self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div/div/div[2]/div/ul/div[4]/ul/li[2]/a")))
        development_module_tab.click()
        print("Navigated to development activity screen")

    def click_create_new(self):
        home_create_new_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div/div/div[1]/button")))
        home_create_new_button.click()
        print("Clicked on create new button")

    def select_new_development(self):
        new_development_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/div/div[4]/p[1]")))
        new_development_option.click()
        print("New development activity selected")

    def enter_project_description(self, description):
        project_desc = self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/main/div/form/div/div/div/div/div[1]/div/div[2]/div[2]/div/div/textarea[1]")))
        project_desc.send_keys(description)
        print("Entered project description")

    def select_dropdown_option(self, dropdown_xpath, option_xpath):
        dropdown = self.driver.find_element(By.XPATH, dropdown_xpath)
        dropdown.click()
        time.sleep(2)
        option = self.wait.until(EC.presence_of_element_located((By.XPATH, option_xpath)))
        option.click()
        print("Dropdown option selected")

    def enter_project_value(self, value):
        project_value = self.driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div/div/div/div/div[1]/div/div[5]/div[2]/div/div/input")
        project_value.send_keys(value)
        print("Entered project value")

    def select_date(self, date_picker_xpath, date_xpath):
        date_picker = self.driver.find_element(By.XPATH, date_picker_xpath)
        date_picker.click()
        date = self.driver.find_element(By.XPATH, date_xpath)
        date.click()
        print("Date selected")

    def enter_location_details(self, district, mandal, village):
        self.enter_text_and_select("/html/body/div/div/main/div/form/div/div/div/div/div[1]/div/div[9]/div[2]/div/div/div/input", district)
        self.enter_text_and_select("/html/body/div/div/main/div/form/div/div/div/div/div[1]/div/div[10]/div[2]/div/div/div/input", mandal)
        self.enter_text_and_select("/html/body/div/div/main/div/form/div/div/div/div/div[1]/div/div[11]/div[2]/div/div/div/input", village)

    def enter_text_and_select(self, field_xpath, text):
        field = self.driver.find_element(By.XPATH, field_xpath)
        field.send_keys(text)
        time.sleep(2)
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ARROW_DOWN).perform()
        actions.send_keys(Keys.ENTER).perform()
        print(f"Selected {text} from dropdown")

    def enter_contact_details(self, contractor_name, contact_name, mobile_number):
        self.driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div/div/div/div/div[1]/div/div[17]/div/div/input").send_keys(contractor_name)
        self.driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div/div/div/div/div[1]/div/div[18]/div/div/input").send_keys(contact_name)
        self.driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div/div/div/div/div[1]/div/div[19]/div/div/input").send_keys(mobile_number)
        print("Entered contact details")

    def submit_development_activity(self):
        submit_button = self.driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div/div/div/div/div[3]/button")
        submit_button.click()
        print("Development activity submitted")
