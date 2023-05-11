from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AccountPage(BasePage):
    invoice_link = (By.XPATH, "/html/body/section/div/div[2]/div[5]/a")


