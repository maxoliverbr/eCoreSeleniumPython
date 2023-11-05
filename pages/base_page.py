""" Base page class definition with methods """


class BasePage:
    """
    BasePage contains methods common to all Page Objects
    """

    def __init__(self, driver):
        self.driver = driver

    def find(self, *locator):
        """
        find method helper function
        :param locator: String
        :return: selenium element
        """
        return self.driver.find_element(*locator)

    def click(self, locator):
        """
        click method helper function
        :param locator: String
        :return: selenium clickable element
        """
        return self.find(*locator).click()

    def set(self, locator, value):
        """
        set method helper function
        :param locator: String
        :param value: String
        :return: None
        """
        self.find(*locator).clear()
        self.find(*locator).send_keys(value)

    def get_text(self, locator):
        """
        get_text helper function
        :param locator: String
        :return: String
        """
        return self.find(*locator).text

    def get_title(self):
        """
        get_title helper function
        :return: String
        """
        return self.driver.title

    def get_current_window(self):
        """
        get_current_window helper function
        :return: Window Handle
        """
        return self.driver.current_window_handle

    def get_windows(self):
        """
        get_windows helper function
        :return: Window handles
        """
        return self.driver.window_handles

    def set_window(self, window):
        """
        set_window helper function
        :param window: Window type
        :return: Window handle
        """
        return self.driver.switch_to.window(window)
