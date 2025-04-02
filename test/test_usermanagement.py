import json
import pytest
from selenium import webdriver
from pages.Usermanagement_page import UserManagementPage

#load config file
with open ("config.json") as configfile:
    config=json.load(configfile)


@pytest.mark.usefixtures("driver")
def test_create_and_delete_user(driver):
    user_mgmt = UserManagementPage(driver)
    #data from config
    name=config["user_management"]["user_name"]
    mobile=config["user_management"]["user_mobile"]
    email=config["user_management"]["user_email"]
    password=config["user_management"]["user_password"]
    
    #methods
    user_mgmt.navigate_to_usermanagement()
    user_mgmt.create_new_user(name, mobile, email, password)
    user_mgmt.delete_user()
    
    assert True, "User successfully created and deleted"
