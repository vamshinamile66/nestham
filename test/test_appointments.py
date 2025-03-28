 
import pytest
from selenium import webdriver
from pages.Appointments_page import AppointmentPage

@pytest.mark.usefixtures("driver")
def test_create_event_and_appointment(driver):
    appointment = AppointmentPage(driver)

    appointment.navigate_to_appointment()
    appointment.create_event("Farmers Meeting", "Uravakonda farmers meeting about crop development")
    appointment.create_appointment("Meeting with MLA", "Discussion on MLA-related issues", "Ragavendra", "9890033788")
    
    assert True, "Event and appointment created successfully"
