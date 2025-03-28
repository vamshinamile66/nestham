import json
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import pytest
from selenium import webdriver
#load json file
with open("config.json") as configfile:
    config=json.load(configfile)

@pytest.fixture(scope="session")
def driver():
    browser=config["browser"].strip().lower()    #remove spaces and case sensitive
    
    if browser=="chrome":
       service=ChromeService(ChromeDriverManager().install())
       driver=webdriver.Chrome(service=service)
    elif browser=="edge":
        service = EdgeService(EdgeChromiumDriverManager().install())
        options = webdriver.EdgeOptions()
        driver = webdriver.Edge(service=service, options=options)
    else:
        raise ValueError(f"unsupported browser:{browser}")
    driver.implicitly_wait(10)  
    yield driver
    driver.quit()
