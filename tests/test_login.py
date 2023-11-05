""" Import test lib """
import pytest

from utilities.test_data import TestData
from pages.login_page import LoginPage
from tests.base_test import BaseTest


class TestLogin(BaseTest):
    """
    Class of test login with test data
    login method with username and password
    return LoginPage object
    """

    def login(self, username, password):
        """ Instantiate LoginPage and login with username and password """
        login_page = LoginPage(self.driver)
        login_page.set_username(username)
        login_page.set_password(password)
        login_page.click_login_button()
        return login_page

    def test_tc001(self):
        """
            TC001 - Login (Positive)
            Goal
            Validate if the user can authenticate in the application with the credentials provided.
        """
        login_page = self.login(TestData.username, TestData.password)
        title = login_page.get_title()
        assert title == TestData.home_page_title

    @pytest.mark.xfail()
    @pytest.mark.parametrize(('username', 'password'), (("Demouser", "abc123"),
                                                        ("demouser_", "xyz"),
                                                        ("demouser", "nananana"),
                                                        ("demouser", "abc123")))
    def test_tc002_parametrized(self, username, password):
        """
        TC002 - Login (Negative)
        Goal
        Validate that the application denies the user login with invalid credentials.

        Known issue last pair of credentials is not invalid ('demouser', 'abc123')

        Test case marked to fail.

        Using fixture with parameters slower due to creating instances for each iteration
        """

        login_page = self.login(username, password)
        alert_message = login_page.get_alert()
        assert alert_message == TestData.alert_message

    @pytest.mark.xfail()
    def test_tc002_non_parametrized(self):
        """ Using TestData class faster """
        for username, password in TestData.username_password_list:
            login_page = self.login(username, password)
            alert_message = login_page.get_alert()
            assert alert_message == TestData.alert_message
