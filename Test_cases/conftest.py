from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == "Chrome":
        driver = webdriver.Chrome()
        print("--launching chrome browser--")
    elif browser == "Firefox":
        driver = webdriver.Firefox()
        print("--launching firefox browser--")
    else:
        driver = webdriver.Edge()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


#### for html report

def pytest_configure(config):
    config._metadata['Project Name'] = 'Nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Amol'


@pytest.hookimpl(tryfirst=True)
def pytest_metadata(metadata):
    metadata.pop("Java_Home", None)
    metadata.pop("Plugins", None)

