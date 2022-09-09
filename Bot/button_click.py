

# Generic button clicks
import time

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By


class Button:

    def __init__(self, browser: webdriver):
        self.browser: webdriver = browser
        self._button = None

    @property
    def button(self):
        return self._button

    @button.setter
    def button(self, value):
        self._button = value

    def find_button(self, by: By, search_string):
        self.button = self.browser.find_element(by, search_string)

    def click_button(self):
        if self.button:
            self.button.click()
            time.sleep(3)

    def check_button_enabled(self) -> bool:

        if self.button:
            return self.button.is_enabled()
        else:
            return False
