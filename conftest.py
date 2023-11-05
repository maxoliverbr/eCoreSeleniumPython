import pytest
from selenium import webdriver
#from selenium.webdriver.remote.remote_connection import RemoteConnection
from utilities.test_data import TestData


"""
Fixture to open the browser instance for each test case.
"""


@pytest.fixture(params=["chrome", "firefox"])
def initialize_driver(request):

    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    elif request.param == "edge":
        driver = webdriver.Edge()
    else:
        driver = webdriver.Chrome()

    driver.implicitly_wait(5)
    request.cls.driver = driver
    # print("Browser: ", request.param)
    driver.get(TestData.url)
    driver.maximize_window()
    yield
    # print("Close Driver")
    driver.close()
