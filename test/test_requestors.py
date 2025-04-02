import json
import pytest
from selenium import webdriver
from pages.Requestors_page import RequestorPage

#load config file
with open ("config.json") as configfile:
    config=json.load(configfile)

@pytest.mark.usefixtures("driver")
def test_create_requestor(driver):
    requestor_page = RequestorPage(driver)
    
    #data from config file
    requestor_firstname=config["requestor_details"]["first_name"]
    requestor_lastname=config["requestor_details"]["last_name"]
    requestor_age=config["requestor_details"]["age"]
    requestor_occupation=config["requestor_details"]["occupation"]
    requestor_mobile=config["requestor_details"]["mobile"]
    requestor_constituency=config["requestor_details"]["constituency"]
    requestor_mandal=config["requestor_details"]["mandal"]
    requestor_village=config["requestor_details"]["village"]
    requestor_tag=config["requestor_details"]["tag"]

    #methods
    requestor_page.template_navigation()
    requestor_page.fill_requestor_details(requestor_firstname,
    requestor_lastname,
    requestor_age,
    requestor_occupation,
    requestor_mobile,
    requestor_constituency,
    requestor_mandal,
    requestor_village,
    requestor_tag )
    
    requestor_page.click_create()

    print("Requestor created successfully!")

