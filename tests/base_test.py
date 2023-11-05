""" Import test lib """
import pytest


@pytest.mark.usefixtures("initialize_driver")
class BaseTest:
    """ Class to trigger initialize driver """
    driver = None
    pass
