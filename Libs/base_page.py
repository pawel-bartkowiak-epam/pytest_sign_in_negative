"""
This module is used for browser's URL interaction
"""


class BasePage():
    """
    Class used for browser's URL interaction
    """

    def __init__(self, driver, base_page_url):
        self.driver = driver
        self.base_page_url = base_page_url

    def navigate_to_url(self, url):
        """
        Navigate to url and verify if page is completely loaded
        :param: url: page url
        """
        self.driver.get(url)
        page_load_state =  \
            self.driver.execute_script('return document.readyState')
        return page_load_state == 'complete'

    def check_current_url(self, expected_url):
        """
        Check if current url matches the expected url
        :param: expected_url: expected page url
        """
        current_url = self.driver.current_url
        return current_url == expected_url
