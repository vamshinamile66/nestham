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
    name = config["template_details"]["name"]
    mandal = config["template_details"]["mandal"]
    constutuency = config["template_details"]["constutuency"]
    studentname = config["template_details"]["student_name"]
    fathername = config["template_details"]["father_name"]
    villagename = config["template_details"]["village_name"]
    mandalname = config["template_details"]["mandal_name"]
    classname = config["template_details"]["class_name"]
    admissionnumber = config["template_details"]["admission_number"]
    schoolname = config["template_details"]["school_name"]
    schooladdress = config["template_details"]["school_address"]

    # Test Steps
    grievance.template_navigation()
    grievance.template_selection()
    grievance.add_requestor(name, constutuency, mandal)
    grievance.template_fill(studentname, fathername, villagename, mandalname, classname, admissionnumber, schoolname, schooladdress)
    grievance.download_attachment()

    print("Grievance form submission successful!")
