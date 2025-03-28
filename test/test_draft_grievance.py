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

    grievance_page.click_create_new()
    grievance_page.click_new_draft()
    grievance_page.fill_grievance_details("Drinking water supply in villages", "8901966840", "Surender")
    grievance_page.click_create_draft()

    print("Draft Grievance created successfully!")
