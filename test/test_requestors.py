import pytest
from selenium import webdriver
from pages.Requestors_page import RequestorPage

@pytest.mark.usefixtures("driver")
def test_create_requestor(driver):
    requestor_page = RequestorPage(driver)
    
    requestor_page.template_navigation()
    requestor_page.fill_requestor_details("Raju", "37", "Actor", "7829636647", "Amidala", "self")
    requestor_page.click_create()

    print("Requestor created successfully!")
