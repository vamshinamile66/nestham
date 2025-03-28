import pytest
from pages.Contact_page import contactsPage
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.mark.usefixtures("driver")
def test_contact_operations(driver):

    contacts_page = contactsPage(driver)
    
    # Navigate to Contacts
    contacts_page.navigate_to_contacts()

    # Add a new contact
    contacts_page.add_new_contact(name="Venkatesh", phone="9500000068", tag="Friend")

    # Search the contact
    contacts_page.search_contact("Venkatesh")

    # Edit the contact's phone number
    contacts_page.edit_contact(new_phone="9446666666")

    # Delete the contact
    contacts_page.delete_contact()

    print("Contact module tests completed successfully!")

