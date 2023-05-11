"""
Provided test data for test cases.
"""

"""
Test data for TC001 and TC002 - login with valid and invalid credentials
"""


class TestData:
    # valid username and passwords
    url = "https://automation-sandbox-python-mpywqjbdza-uc.a.run.app/"
    username = "demouser"
    password = "abc123"

    # invalid username and passwords
    # known issue last pair of tuples should be invalid - requirements change necessary
    username_password_list = [("Demouser", "abc123"),
                              ("demouser_", "xyz"),
                              ("demouser", "nananana"),
                              ("demouser", "abc123")]

    # alert message of invalid login
    alert_message = "Wrong username or password."

    # home page title
    home_page_title = "Automation Example"


"""
Test data for TC003 - Invoice
"""


class TestDataInvoice:
    username = TestData.username
    password = TestData.password
    hotel_name = "Rendezvous Hotel"
    invoice_date = "14/01/2018"
    due_date = "15/01/2018"
    invoice_number = "110"
    booking_code = "0875"
    customer_details = "JOHNY SMITH\nR2, AVENUE DU MAROC\n123456"
    room = "Superior Double"
    check_in = "14/01/2018"
    check_out = "15/01/2018"
    total_stay_count = "1"
    total_stay_amount = "$150"
    deposit_now = "USD $20.90"
    tax_vat = "USD $19.00"
    total_amount = "USD $209.00"
