"""
This module is used for sign in page objects
"""

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Libs.base_page import BasePage
from Locators.sign_in_locators import SignInLocators


class SignInPageObjects(BasePage):
    """
    Class used for sign in page objects
    """

    def __init__(self, driver):
        self.driver = driver
        self._timeout = 10

    def enter_credential(self, credential_type, credential_value):
        """
        Enter credential
        :param: credential_type: email/password
        :param: credential_value: email or password value
        """
        if credential_type == "email":
            locator = SignInLocators.locator_email_login
        elif credential_type == "password":
            locator = SignInLocators.locator_password_login
        else:
            raise ValueError("Invalid credential type. Valid types are 'email' or 'password'.")

        element = WebDriverWait(self.driver, self._timeout).until(
            EC.element_to_be_clickable((locator)))
        element.click()
        element.clear()
        element.send_keys(credential_value)

    def check_is_invalid_email(self):
        """
        Check if Invalid Email message appears
        """
        try:
            self.driver.find_element(SignInLocators.locator_invalid_email_login)
        except NoSuchElementException:
            return False
        return True

    def click_sign_in_button(self):
        """
        Click sign me in button
        """
        element = WebDriverWait(self.driver, self._timeout).until(
            EC.element_to_be_clickable((SignInLocators.locator_email_login)))
        element.click()
