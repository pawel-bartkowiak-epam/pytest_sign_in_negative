"""
This file contains fixtures that are automatically discovered and used by pytest.
"""

import pytest

from selenium import webdriver


@pytest.fixture(scope='session')
def driver():
    """
    Fixture function to provide a WebDriver instance for testing.
    """
    web_driver = webdriver.Firefox()
    yield web_driver
    web_driver.quit()


@pytest.fixture
def base_page_url(pytestconfig):
    """
    Fixture function to retrieve base page url from pytest configuration.
    """
    return pytestconfig.getoption("base_page_url")


def pytest_addoption(parser):
    """
    Hook function to add a command-line option for setting base page url.
    """
    parser.addoption("--base_page_url", action="store", default="https://www.browserstack.com")
