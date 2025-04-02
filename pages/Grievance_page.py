from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GrievancePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Explicit wait
    
    # Locators
    home_create_new_button = (By.XPATH, "//*[@id='root']/div/div/div/div/div[1]/button")
    new_grievance_option = (By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/p[1]")
    template_dropdown = (By.XPATH, "/html/body/div/div/main/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div/div")
    template_option = (By.XPATH, "/html/body/div[2]/div[3]/ul/li[2]")
    next_button_template = (By.XPATH, "/html/body/div/div/main/div/div[2]/div/div[3]/div[1]/div/button[2]")
    
    add_new_requestor = (By.XPATH, "/html/body/div/div/main/div/div[2]/div/div[2]/div[3]/div/div/div/div/div[1]/div/button")
    requestor_constutuency_dropdown=(By.XPATH,"/html/body/div[2]/div[3]/div/div[1]/div/div[1]/div[1]/div/div/div/input")
    requestor_mandal_dropdown = (By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/div/div[1]/div[2]/div/div/div/input")
    requestor_name_search = (By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/div/div[1]/div[3]/div[1]/div/div/input")
    requestor_search_icon = (By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/div/div[1]/div[3]/div[1]/div/div/div[2]/button")
    requestor_search_result = (By.XPATH, "//input[@type='radio']")
    select_requestor_button = (By.XPATH, "/html/body/div[2]/div[3]/div/div[2]/div/div/div/button")
    
    
    student_name = (By.XPATH, "//label[contains(text(), 'Student Name')]/following-sibling::div//input")
    father_name = (By.XPATH, "//label[contains(text(), 'Father Name')]/following-sibling::div//input")
    village_name = (By.XPATH, "//label[contains(text(), 'Village Name')]/following-sibling::div//input")
    mandal_name = (By.XPATH, "//label[contains(text(), 'Mandal Name')]/following-sibling::div//input")
    class_name = (By.XPATH, "//label[contains(text(), 'Class')]/following-sibling::div//input")
    admission_number = (By.XPATH, "//label[contains(text(), 'Admission No')]/following-sibling::div//input")
    school_name = (By.XPATH, "//label[contains(text(), 'School Name')]/following-sibling::div//input")
    school_address = (By.XPATH, "//label[contains(text(), 'School Address')]/following-sibling::div//textarea")
    
    save_template_button = (By.XPATH, "//button[contains(text(),'Save details')]" )
    create_grievance_button = (By.XPATH, "//button[contains(text(),'Create Request')]" )
    
    attachment_toggle = (By.XPATH, "/html/body/div/div/main/div/div[2]/div[1]/div/div[1]/div/div[2]/div/div[2]/div[3]/div[1]/div[1]" )
    view_attachments = (By.XPATH, "/html/body/div/div/main/div/div[2]/div[1]/div/div[1]/div/div[2]/div/div[2]/div[3]/div[2]/div/div/div/div[2]/div/div/div/div/div/div/div" )
    download_attachment_doc = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div[1]/div[2]/button[1]" )
    close_attchement_popup=(By.XPATH,"/html/body/div[2]/div[3]/div/div/div[1]/div[2]/button[2]")
    # Methods
    def template_navigation(self):
        self.wait.until(EC.element_to_be_clickable(self.home_create_new_button)).click()
        self.wait.until(EC.element_to_be_clickable(self.new_grievance_option)).click()
    
    def template_selection(self):
        self.wait.until(EC.element_to_be_clickable(self.template_dropdown)).click()
        self.wait.until(EC.element_to_be_clickable(self.template_option)).click()
        self.wait.until(EC.element_to_be_clickable(self.next_button_template)).click()
        
    
    def add_requestor(self, name,constutuency, mandal):
        self.wait.until(EC.element_to_be_clickable(self.add_new_requestor)).click()
        time.sleep(5)
        constituency_dropdown=self.wait.until(EC.element_to_be_clickable(self.requestor_constutuency_dropdown))
        constituency_dropdown.send_keys(constutuency)
        actions = ActionChains(self.driver)
        time.sleep(1)
        actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.RETURN).perform()
        mandal_dropdown = self.wait.until(EC.element_to_be_clickable(self.requestor_mandal_dropdown))
        mandal_dropdown.send_keys(mandal)
        actions = ActionChains(self.driver)
        time.sleep(1)
        actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.RETURN).perform()


      

        self.wait.until(EC.presence_of_element_located(self.requestor_name_search))
        self.wait.until(EC.element_to_be_clickable(self.requestor_name_search)).send_keys(name)

        
        self.wait.until(EC.element_to_be_clickable(self.requestor_search_icon)).click()
        self.wait.until(EC.element_to_be_clickable(self.select_requestor_button)).click()
        self.wait.until(EC.element_to_be_clickable(self.next_button_template)).click()
    
    def template_fill(self, studentname, fathername, villagename, mandalname, classname, admissionnumber, schoolname, schooladdress):
        fields = [
            (self.student_name, studentname),
            (self.father_name, fathername),
            (self.village_name, villagename),
            (self.mandal_name, mandalname),
            (self.class_name, classname),
            (self.admission_number, admissionnumber),
            (self.school_name, schoolname),
            (self.school_address, schooladdress)
        ]
        
        for locator, value in fields:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.clear()
            element.send_keys(value)
        
        self.wait.until(EC.element_to_be_clickable(self.save_template_button)).click()
        self.wait.until(EC.element_to_be_clickable(self.next_button_template)).click()
        self.wait.until(EC.element_to_be_clickable(self.create_grievance_button)).click()
    
    def download_attachment(self):
        self.wait.until(EC.element_to_be_clickable(self.attachment_toggle)).click()
        self.wait.until(EC.element_to_be_clickable(self.view_attachments)).click()
        self.wait.until(EC.element_to_be_clickable(self.download_attachment_doc)).click()
        self.wait.until(EC.element_to_be_clickable(self.close_attchement_popup)).click()
        time.sleep(5)
        
