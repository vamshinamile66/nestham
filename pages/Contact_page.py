from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class contactsPage:

    def __init__(self, driver):
        self.driver = driver

        self.contacts_tab = (By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div/ul/div[3]/ul/li[3]/a/div/div')
        self.add_contact_button = (By.XPATH, '/html/body/div/div/main/div/div/div[1]/div/div/div[2]/div/button')
        self.name_field = (By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/div/div[1]/div/div/input")
        self.phone_add_icon = (By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div/div[1]/button/span[1]")
        self.phone_input = (By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/div/div/input")
        self.tag_field = (By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/div/div[4]/div/div/div/input")
        self.submit_button = (By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/button')
        self.search_input = (By.XPATH, "/html/body/div/div/main/div/div/div[2]/div/div[1]/div/div[1]/div/div/input")
        self.edit_button = (By.XPATH, "/html/body/div/div/main/div/div/div[2]/div/div[1]/div/div[2]/div[1]/ul/li[1]/div[3]/div/button[2]")
        self.delete_button = (By.XPATH, "/html/body/div/div/main/div/div/div[2]/div/div[1]/div/div[2]/div[1]/ul/li[1]/div[3]/div/button[1]")
        self.confirm_delete_button = (By.XPATH, "/html/body/div[2]/div[3]/div/div[2]/button[2]")

    def navigate_to_contacts(self):
        """Navigate to the Contacts tab."""
        self.driver.find_element(*self.contacts_tab).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Contacts')]"))
        )

    def add_new_contact(self, name, phone, tag):
        """Add a new contact."""
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.add_contact_button)).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.name_field)).send_keys(name)
        self.driver.find_element(*self.phone_add_icon).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.phone_input)).send_keys(phone)
        self.driver.find_element(*self.tag_field).send_keys(tag)
        self.driver.find_element(*self.submit_button).click()

    def search_contact(self, name):
        """Search for a contact by name."""
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.search_input)).send_keys(name)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{name}')]")))

    def edit_contact(self, new_phone):
        """Edit the contact's phone number."""
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.edit_button)).click()
        phone_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.phone_input))
        phone_field.clear()
        phone_field.send_keys(new_phone)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div[2]/button").click()

    def delete_contact(self):
        """Delete a contact."""
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.delete_button)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.confirm_delete_button)).click()

