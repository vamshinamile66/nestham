 
import pytest
from pages.Development_activity_page import DevelopmentPage

@pytest.mark.usefixtures("setup")
class TestDevelopment:
    def test_create_development_activity(self, setup):
        driver = setup
        dev_page = DevelopmentPage(driver)

        # Navigate to Development module
        dev_page.navigate_to_development_tab()

        # Create new development activity
        dev_page.click_create_new()
        dev_page.select_new_development()

        # Fill in project details
        dev_page.enter_project_description("Cycles distribution in UKD villages")
        dev_page.select_dropdown_option("/html/body/div/div/main/div/form/div/div/div/div/div[1]/div/div[3]/div[2]/div", "/html/body/div[2]/div[3]/ul/li[5]")  # Select department
        dev_page.select_dropdown_option("/html/body/div/div/main/div/form/div/div/div/div/div[1]/div/div[4]/div[2]/div/div", "/html/body/div[2]/div[3]/ul/li[2]")  # Select type
        dev_page.enter_project_value("100")

        # Select project dates
        dev_page.select_date("/html/body/div/div/main/div/form/div/div/div/div/div[1]/div/div[6]/div[2]/div/div[1]/div/div/button", "/html/body/div[2]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[3]/button[6]")  # From Date
        dev_page.select_date("/html/body/div/div/main/div/form/div/div/div/div/div[1]/div/div[6]/div[2]/div/div[2]/div/div/button", "/html/body/div[2]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[4]/button[7]")  # End Date

        # Enter location details
        dev_page.enter_location_details("Bapatla", "Cherukupalli", "Gudavalli")

        # Enter contact details
        dev_page.enter_contact_details("ossi", "ganesh", "9056677944")

        # Submit development activity
        dev_page.submit_development_activity()
