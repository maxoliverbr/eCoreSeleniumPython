""" Driver initializer trigger """
import pytest


@pytest.mark.usefixtures("initialize_driver")
class BaseTest: # pylint: disable=too-few-public-methods
    """ Class to trigger initialize driver """
    driver = None
