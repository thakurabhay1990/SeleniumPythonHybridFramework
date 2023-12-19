import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from utilities import ReadConfigurations


@pytest.fixture()
def setup_and_teardown(request):
    browser = ReadConfigurations.read_configuration("basic info","browser")
    driver = None
    if browser.__eq__("chrome"):
        service_obj = Service("/Users/abhaythakur/Downloads/drivers/chromedriver")
        driver = webdriver.Chrome(service=service_obj)
    elif browser.__eq__("firefox"):
        service_obj = Service("/Users/abhaythakur/Downloads/drivers/geckodriver")
        driver = webdriver.Firefox(service=service_obj)
    elif browser.__eq__("edge"):
        service_obj = Service("/Users/abhaythakur/Downloads/drivers/msedgedriver")
        driver = webdriver.Edge(service=service_obj)
    else:
        print("Please provide a valid browser name like : chrome, firefox or edge")

    driver.maximize_window()
    app_url = ReadConfigurations.read_configuration("basic info", "url")
    driver.get(app_url)
    request.cls.driver = driver
    yield
    driver.quit()
