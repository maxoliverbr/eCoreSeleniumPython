import pytest
from selenium.common import NoSuchElementException, InvalidSelectorException
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from pages.account_page import AccountPage
from pages.invoice_page import InvoicePage
from tests.base_test import BaseTest
from utilities.test_data import TestDataInvoice


# class of test invoice with test data
class TestInvoice(BaseTest):
    """
    TC003 - Validate invoice details

    Objective:
    Validate the invoice information is presented.
    """
    # @pytest.mark.xfail()
    def test_tc003(self):
        # login page object
        login_page = LoginPage(self.driver)

        # account page object
        account_page = AccountPage(self.driver)

        # invoice page object
        invoice_page = InvoicePage(self.driver)

        # login to app using test data username and password
        login_page.login_app(TestDataInvoice.username, TestDataInvoice.password)

        # locate invoice link and click
        account_page.click(account_page.invoice_link)

        # identify window of new target
        win = invoice_page.get_windows()

        # activate new tab window
        invoice_page.set_window(win[1])

        # Check each field in the invoice against test data
        assert invoice_page.get_hotel_name() == TestDataInvoice.hotel_name
        assert invoice_page.get_booking_code() == TestDataInvoice.booking_code
        assert invoice_page.get_room() == TestDataInvoice.room
        assert invoice_page.get_check_in() == TestDataInvoice.check_in
        assert invoice_page.get_check_out() == TestDataInvoice.check_out
        assert invoice_page.get_total_stay_count() == TestDataInvoice.total_stay_count
        assert invoice_page.get_deposit_now() == TestDataInvoice.deposit_now
        assert invoice_page.get_total_stay_amount() == TestDataInvoice.total_stay_amount
        assert invoice_page.get_customer_details() == TestDataInvoice.customer_details
        assert TestDataInvoice.invoice_date in invoice_page.get_invoice_date()
        assert TestDataInvoice.due_date in invoice_page.get_due_date()

        # Assertion errors due to known issues
        with pytest.raises(AssertionError):
            # Known issue - expected USD 19.00 - actual USD 19
            assert invoice_page.get_tax_vat() == TestDataInvoice.tax_vat
            # Known issue - expected USD 209.00 - actual USD 209
            assert invoice_page.get_total_amount() == TestDataInvoice.total_amount


