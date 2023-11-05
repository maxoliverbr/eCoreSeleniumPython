""" Import Selenium By for element selection """
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AccountPage(BasePage):
    """
    Account page class extends BasePage with XPATH selector
    """
    invoice_link = (By.XPATH, "/html/body/section/div/div[2]/div[5]/a")
