from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.account_page import AccountPage

"""
Login base page with related methods:
set_username
set_password
click_login_button
login_app
get_alert
"""


class LoginPage(BasePage):
    # login related locators
    username = (By.NAME, "username")
    password = (By.NAME, "password")
    login_button = (By.ID, "btnLogin")
    alert_message = (By.XPATH, "//div[@role='alert']")

    def __init__(self, driver):
        super().__init__(driver)

    def set_username(self, username):
        self.set(self.username, username)

    def set_password(self, password):
        self.set(self.password, password)

    def click_login_button(self, ):
        self.click(self.login_button)
        return AccountPage(self.driver)

    def login_app(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.click_login_button()
        return AccountPage(self.driver)

    def get_alert(self):
        return self.get_text(self.alert_message)
