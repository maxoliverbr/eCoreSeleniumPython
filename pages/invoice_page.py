from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InvoicePage(BasePage):
    """
    Locators for invoice elements
    """
    hotel_name = (By.XPATH, "//h4[@class='mt-5']")
    invoice_number = (By.XPATH, "//h6[contains(text(),'Invoice #')]")
    booking_code = (By.XPATH, "//td[text()='Booking Code']//following-sibling::td[1]")
    room = (By.XPATH, "//td[text()='Room']//following-sibling::td[1]")
    check_in = (By.XPATH, "//td[text()='Check-In']//following-sibling::td[1]")
    check_out = (By.XPATH, "//td[text()='Check-Out']//following-sibling::td[1]")
    total_stay_count = (By.XPATH, "//td[text()='Total Stay Count']//following-sibling::td[1]")
    total_stay_amount = (By.XPATH, "//td[text()='Total Stay Amount']//following-sibling::td[1]")
    deposit_now = (By.XPATH, "//h5[text()='Billing Details']//following-sibling::table/tbody/tr/td[1]")
    tax_vat = (By.XPATH, "//h5[text()='Billing Details']//following-sibling::table/tbody/tr/td[2]")
    total_amount = (By.XPATH, "//h5[text()='Billing Details']//following-sibling::table/tbody/tr/td[3]")

    # Improve locators suggestion
    invoice_date = (By.XPATH, "/html/body/section/div/ul/li[1]")
    due_date = (By.XPATH, "/html/body/section/div/ul/li[2]")
    customer_details = (By.XPATH, "/html/body/section/div/div")

    def __init__(self, driver):
        super().__init__(driver)

    def get_hotel_name(self):
        return self.get_text(self.hotel_name)

    def get_invoice_date(self):
        return self.get_text(self.invoice_date)

    def get_due_date(self):
        return self.get_text(self.due_date)

    def get_booking_code(self):
        return self.get_text(self.booking_code)

    def get_customer_details(self):
        return self.get_text(self.customer_details)

    def get_room(self):
        return self.get_text(self.room)

    def get_check_in(self):
        return self.get_text(self.check_in)

    def get_check_out(self):
        return self.get_text(self.check_out)

    def get_total_stay_count(self):
        return self.get_text(self.total_stay_count)

    def get_total_stay_amount(self):
        return self.get_text(self.total_stay_amount)

    def get_deposit_now(self):
        return self.get_text(self.deposit_now)

    def get_tax_vat(self):
        return self.get_text(self.tax_vat)

    def get_total_amount(self):
        return self.get_text(self.total_amount)

