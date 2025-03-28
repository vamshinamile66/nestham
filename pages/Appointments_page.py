import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AppointmentPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # Locators
    APPOINTMENT_TAB = (By.XPATH, "//div[4]/ul/li[1]/a")
    CREATE_EVENT_BUTTON = (By.XPATH, "//button[contains(text(),'Create Event')]")
    EVENT_TITLE_INPUT = (By.XPATH, "//input[@placeholder='Enter Event Title Here']")
    EVENT_DETAILS_INPUT = (By.XPATH, "//textarea[@placeholder='Enter Event Details Here']")
    SUBMIT_EVENT_BUTTON = (By.XPATH, "/html/body/div[2]/div[3]/div/div[2]/div/div[2]/button[2]")

    CREATE_APPOINTMENT_BUTTON = (By.XPATH, "/html/body/div/div/main/div/div[2]/div[2]/div/div[2]/button[5]")
    APPOINTMENT_SUBJECT_INPUT = (By.XPATH, "//input[@placeholder='Enter Subject Here']")
    APPOINTMENT_DETAILS_INPUT = (By.XPATH, "//textarea[@placeholder='Enter Appointment Details Here']")
    ADD_ATTENDEE_BUTTON = (By.XPATH, "//button[contains(text(),' + Add Attendees')]")
    ATTENDEE_NAME_INPUT = (By.XPATH, "//input[@placeholder='Enter Name Here']")
    ATTENDEE_MOBILE_INPUT = (By.XPATH, "//input[@placeholder='Enter Mobile Number']")
    SUBMIT_APPOINTMENT_BUTTON = (By.XPATH, "//button[contains(text(),'Create Appointment')]")

    # Methods
    def navigate_to_appointment(self):
        self.wait.until(EC.element_to_be_clickable(self.APPOINTMENT_TAB)).click()

    def create_event(self, title, details):
        self.wait.until(EC.element_to_be_clickable(self.CREATE_EVENT_BUTTON)).click()
        self.wait.until(EC.presence_of_element_located(self.EVENT_TITLE_INPUT)).send_keys(title)
        self.wait.until(EC.presence_of_element_located(self.EVENT_DETAILS_INPUT)).send_keys(details)
        try:
           self.wait.until(EC.element_to_be_clickable(self.SUBMIT_EVENT_BUTTON)).click()
        except InterruptedError as e:
            print("Event is not created due to {e}")


    def create_appointment(self, subject, details, attendee_name, attendee_mobile):
        time.sleep(5)
        self.wait.until(EC.element_to_be_clickable(self.CREATE_APPOINTMENT_BUTTON)).click()
        self.wait.until(EC.presence_of_element_located(self.APPOINTMENT_SUBJECT_INPUT)).send_keys(subject)
        self.wait.until(EC.presence_of_element_located(self.APPOINTMENT_DETAILS_INPUT)).send_keys(details)
        
        self.wait.until(EC.element_to_be_clickable(self.ADD_ATTENDEE_BUTTON)).click()
        self.wait.until(EC.presence_of_element_located(self.ATTENDEE_NAME_INPUT)).send_keys(attendee_name)
        self.wait.until(EC.presence_of_element_located(self.ATTENDEE_MOBILE_INPUT)).send_keys(attendee_mobile)
        
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_APPOINTMENT_BUTTON)).click()
