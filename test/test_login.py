import json
import pytest
from pages.Login_page import LoginPage

# Load configuration from config.json
with open("config.json") as config_file:
    config = json.load(config_file)

@pytest.mark.usefixtures("driver")
def test_login_function(driver):
    driver.get(config["base_url"])
    
    # Get credentials from config file
    username = config["username"]
    password = config["password"]
    
    # Initialize login page and perform login
    login_page = LoginPage(driver)
    login_page.login(username, password)

    print("Login test executed successfully!")
