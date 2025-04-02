import json
import pytest
from selenium import webdriver
from pages.Draft_grievance_page import GrievancePage

# Load configuration from config.json
with open("config.json") as config_file:
    config = json.load(config_file)

@pytest.mark.usefixtures("driver")
def test_create_draft_grievance(driver):
    grievance_page = GrievancePage(driver)
    #load data from json file
    grievancedesc=config["draft_grievance"]["grievance_desc"]
    draft_requestor_mobile=config["draft_grievance"]["draft_requestor_mobile"]
    draft_requestor_name=config["draft_grievance"]["draft_requestor_name"]
    #methods
    grievance_page.click_create_new()
    grievance_page.click_new_draft()
    grievance_page.fill_grievance_details(grievancedesc, draft_requestor_mobile, draft_requestor_name)
    grievance_page.click_create_draft()

    print("Draft Grievance created successfully!")
