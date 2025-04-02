import json
import pytest
from pages.Contact_page import contactsPage
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Load configuration from config.json
with open("config.json") as config_file:
    config = json.load(config_file)
    
@pytest.mark.usefixtures("driver")
def test_contact_operations(driver):

    contacts_page = contactsPage(driver)
    
    # Navigate to Contacts
    contacts_page.navigate_to_contacts()

    contact_name=config["contact_details"]["contact_name"]
    contact_phone=config["contact_details"]["contact_phone"]
    contact_tag=config["contact_details"]["contact_tag"]
    contact_new_phone=config["contact_details"]["contact_new_phone"]
    contact_search=config["contact_details"]["contact_search"]
   

    # Add a new contact
    contacts_page.add_new_contact(contact_name, contact_phone, contact_tag)

    # Search the contact
    contacts_page.search_contact(contact_name)

    # Edit the contact's phone number
    contacts_page.edit_contact(contact_new_phone)

    # Delete the contact
    contacts_page.delete_contact()

    print("Contact module tests completed successfully!")

