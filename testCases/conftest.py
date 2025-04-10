# import pytest
#
# from selenium import webdriver
#
# @pytest.fixture()
# def setup():
#     driver = webdriver.Firefox()
#     driver.implicitly_wait(10)
#     driver.maximize_window()
#     return driver


import pytest

from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser")


# Define the browser fixture function with a single argument, request.
# Within the browser function, use the request.config.getoption() method to get the value of the --browser option passed to pytest on the command line.
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome Browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox Browser")
    elif browser == 'edge':
        print("Launching Edge Browser")
        driver = webdriver.Edge()
    else:
        print("Headless mode")
        chrome_options = webdriver.FirefoxOptions()
        # chrome_options.add_argument("headless")
        driver = webdriver.Chrome(options=chrome_options)
    # driver.implicitly_wait(10)
    driver.maximize_window()
    return driver


















@pytest.fixture(params=[
    ("standard_user","secret_sauce","Pass"),
    ("standard_user1","secret_sauce","Fail"),
    ("standard_user", "secret_sauce1", "Fail"),
    ("standard_user12", "secret_sauce21", "Fail")

])

def  getDataforlogin(request):
    return request.param



