""" Login Page class definition """
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.account_page import AccountPage



class LoginPage(BasePage):
    """
    Login base page with related methods:
    set_username
    set_password
    click_login_button
    login_app
    get_alert
    login related locators
    """
    username = (By.NAME, "username")
    password = (By.NAME, "password")
    login_button = (By.ID, "btnLogin")
    alert_message = (By.XPATH, "//div[@role='alert']")

    def __init__(self, driver):
        super().__init__(driver)

    def set_username(self, username):
        """
        set_username helper function
        :param username: String
        :return: None
        """
        self.set(self.username, username)

    def set_password(self, password):
        """
        set_password helper function
        :param password: String
        :return: None
        """
        self.set(self.password, password)

    def click_login_button(self):
        """
        click_login_button helper function
        :return: None
        """
        self.click(self.login_button)
        return AccountPage(self.driver)

    def login_app(self, username, password):
        """
        login_app helper function
        :param username: String
        :param password: String
        :return: AccountPage
        """
        self.set_username(username)
        self.set_password(password)
        self.click_login_button()
        return AccountPage(self.driver)

    def get_alert(self):
        """
        get_alert helper function
        :return: String
        """
        return self.get_text(self.alert_message)
