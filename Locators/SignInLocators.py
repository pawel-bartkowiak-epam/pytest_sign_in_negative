"""
This module is used for sign in locators
"""

from selenium.webdriver.common.by import By


class SignInLocators:
    """
    Class used for sign in locators
    """

    locator_email_login = (By.XPATH, '//input[@id="user_email_login"]')
    locator_invalid_email_login = (By.XPATH, '//span[contains(.,"Invalid Email")]')
    locator_password_login = (By.XPATH, '//input[@id="user_password"]')
    locator_sign_me_in_button = (By.XPATH, '//input[@value="Sign me in"]')
