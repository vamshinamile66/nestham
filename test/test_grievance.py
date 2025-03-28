import json
import pytest
from pages.Grievance_page import GrievancePage

# Load configuration from config.json
with open("config.json") as config_file:
    config = json.load(config_file)

@pytest.mark.usefixtures("driver")
def test_grievance_create(driver):
    grievance = GrievancePage(driver)

    # Data from config.json
    name = config["name"]
    mandal = config["mandal"]
    studentname = config["studentname"]
    fathername = config["fathername"]
    villagename = config["villagename"]
    mandalname = config["mandalname"]
    classname = config["classname"]
    admissionnumber = config["admissionnumber"]
    schoolname = config["schoolname"]
    schooladdress = config["schooladdress"]

    # Test Steps
    grievance.template_navigation()
    grievance.template_selection()
    grievance.add_requestor(name, mandal)
    grievance.template_fill(studentname, fathername, villagename, mandalname, classname, admissionnumber, schoolname, schooladdress)
    grievance.download_attachment()

    print("Grievance form submission successful!")
