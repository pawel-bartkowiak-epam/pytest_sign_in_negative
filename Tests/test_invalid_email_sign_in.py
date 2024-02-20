"""
This module is used for testing signing in
"""
import json

from PageObjects.SignInPageObjects import SignInPageObjects
from Libs.BasePage import BasePage


def test_invalid_email_sign_in(driver, base_page_url):
    """
    Test case testing signing in with incorrect email address
    """
    base_page = BasePage(driver, base_page_url)
    sign_in_page = SignInPageObjects(driver)

    with open('test_utils/invalid_credentials.json') as json_file:
        credentials = json.load(json_file)
        invalid_email = credentials['email']
        password = credentials['password']

    base_page.navigate_to_url(f"{base_page_url}/users/sign_in")
    sign_in_page.enter_credential("email", invalid_email)
    assert sign_in_page.check_is_invalid_email
    sign_in_page.enter_credential("password", password)
    sign_in_page.click_sign_in_button()
    assert base_page.check_current_url(f"{base_page_url}/users/sign_in")
