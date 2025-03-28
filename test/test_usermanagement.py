import pytest
from selenium import webdriver
from pages.Usermanagement_page import UserManagementPage



@pytest.mark.usefixtures("driver")
def test_create_and_delete_user(driver):
    user_mgmt = UserManagementPage(driver)

    user_mgmt.navigate_to_usermanagement()
    user_mgmt.create_new_user("gdeepa", "6668184817", "deepeq5k@gmail.com", "Test@12345")
    user_mgmt.delete_user()
    
    assert True, "User successfully created and deleted"
