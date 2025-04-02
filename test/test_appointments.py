 

import json
import pytest
from selenium import webdriver
from pages.Appointments_page import AppointmentPage


#load config file
with open("config.json") as config_file:
    config = json.load(config_file)

@pytest.mark.usefixtures("driver")
def test_create_event_and_appointment(driver):
    appointment = AppointmentPage(driver)
    #data from config file
    eventTitle=config["appointment_details"]["event_title"]
    eventDetails=config["appointment_details"]["event_details"]
    appointmentSubject=config["appointment_details"]["appointment_subject"]
    appointmentDetails=config["appointment_details"]["appointment_details"]
    attendeeName=config["appointment_details"]["attendee_name"]
    attendeeMobileNnumber=config["appointment_details"]["attendee_mobile_number"]

    #methods
    appointment.navigate_to_appointment()
    appointment.create_event(eventTitle, eventDetails)
    appointment.create_appointment(appointmentSubject, appointmentDetails, attendeeName, attendeeMobileNnumber)
    
    assert True, "Event and appointment created successfully"
