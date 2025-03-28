from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class RequestorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.actions = ActionChains(driver)

    # Locators
    #REQUESTOR_TAB = (By.XPATH, "/html/body/div/div/div/div/div/div[2]/div/ul/div[3]/ul/li[1]/a/div/div")
    home_create_new_button = (By.XPATH, "/html/body/div/div/div/div/div/div[1]/button")
    NEW_REQUESTOR=(By.XPATH,"/html/body/div[2]/div[3]/div/div[2]/p[1]")
    FIRST_NAME_INPUT=(By.XPATH,"/html/body/div/div/main/div/div/div[2]/form/div[1]/div[1]/div[1]/div[2]/div/div[1]/div/div/input")
    LAST_NAME_INPUT = (By.XPATH, "/html/body/div/div/main/div/div/div[2]/form/div[1]/div[1]/div[1]/div[2]/div/div[2]/div/div/input")
    AGE_INPUT = (By.XPATH, "/html/body/div/div/main/div/div/div[2]/form/div[1]/div[1]/div[1]/div[2]/div/div[3]/div/div/input")
    OCCUPATION_INPUT = (By.XPATH, "/html/body/div/div/main/div/div/div[2]/form/div[1]/div[1]/div[1]/div[2]/div/div[5]/div[1]/div/div/input")
    MOBILE_NUMBER_INPUT = (By.XPATH, "/html/body/div/div/main/div/div/div[2]/form/div[1]/div[1]/div[1]/div[2]/div/div[6]/div/div/input")
    CONSTITUENCY_INPUT=(By.XPATH,"/html/body/div/div/main/div/div/div[2]/form/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/div/div/input")
    MANDAL_INPUT=(By.XPATH,"/html/body/div/div/main/div/div/div[2]/form/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/div/div/input")
    VILLAGE_INPUT = (By.XPATH, "/html/body/div/div/main/div/div/div[2]/form/div[1]/div[1]/div[2]/div[2]/div/div[3]/div/div/div/input")
    TAG_INPUT = (By.XPATH, "/html/body/div/div/main/div/div/div[2]/form/div[1]/div[1]/div[4]/div[2]/div/div/div/div/input")
    CREATE_BUTTON = (By.XPATH, "/html/body/div/div/main/div/div/div[2]/div[2]/div[2]/button[2]")

    # Actions
    #def click_requestor_tab(self):
    #    self.wait.until(EC.element_to_be_clickable(self.REQUESTOR_TAB)).click()

    def template_navigation(self):
        self.wait.until(EC.element_to_be_clickable(self.home_create_new_button)).click()
        self.wait.until(EC.element_to_be_clickable(self.NEW_REQUESTOR)).click()

    def enter_text(self, locator, text):
        self.wait.until(EC.presence_of_element_located(locator)).send_keys(text)

    def select_from_dropdown(self, locator, text):
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.send_keys(text)
        self.actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

    def fill_requestor_details(self,firsrname, last_name, age, occupation, mobile, constituency, mandal, village, tag):
        self.enter_text(self.FIRST_NAME_INPUT, firsrname)
        self.enter_text(self.LAST_NAME_INPUT, last_name)
        self.enter_text(self.AGE_INPUT, age)
        self.select_from_dropdown(self.OCCUPATION_INPUT, occupation)
        self.enter_text(self.MOBILE_NUMBER_INPUT, mobile)
        self.select_from_dropdown(self.C, constituency)
        self.select_from_dropdown(self., mandal)
        self.select_from_dropdown(self.VILLAGE_INPUT, village)
        self.select_from_dropdown(self.TAG_INPUT, tag)

    def click_create(self):
        self.wait.until(EC.element_to_be_clickable(self.CREATE_BUTTON)).click()


