

# Generic button clicks
import time

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

from Bot.browser import Browser


class Button(Browser):

    def __init__(self, browser: webdriver):
        super().__init__(browser)
        # self.browser: webdriver = browser
        # Key value, of button type and button
        # Needed to store information
        self._button: dict = {}

    @property
    def button(self) -> dict:
        return self._button

    @button.setter
    def button(self, button_dict: dict):
        self._button.update(button_dict)

    def find_button(self, by: By, search_string, button_key: str = "travel"):

        try:
            button = self.browser.find_element(by, search_string)
            self.button = {
                button_key: button
            }
        except Exception as e:
            raise

    def click_button(self, button_key: str = "travel"):
        # if self.button:
        #     self.button.click()
        #     time.sleep(3)

        if self.button.get(button_key):
            self.button.get(button_key).click()
            time.sleep(3)

    def check_button_enabled(self, button_key: str = "travel") -> bool:

        if self.button.get(button_key):
            return self.button.get(button_key).is_enabled()
        else:
            return False

    def find_go_back_button(self, by: By, search_string):
        try:
            self.find_button(by, search_string, "exit")
        except:
            raise