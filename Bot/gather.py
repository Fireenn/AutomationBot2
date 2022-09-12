from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

from Bot.button_click import Button


class Gather(Button):

    def __init__(self, browser: webdriver):

        super().__init__(browser)
        self.button_type = "gather"
        self._can_gather = False

    @property
    def can_gather(self):
        return self._can_gather

    @can_gather.setter
    def can_gather(self, value):
        self._can_gather = value

    def execute(self):

        # self.click_button(self.button_type)
        try:
            self.find_button(By.ID, "crafting_button", self.button_type)
            # self.check_button_enabled(self.button_type)
            self.check_can_gather()

            while self.check_button_enabled(self.button_type) and self.can_gather:
                self.click_button(self.button_type)
                self.check_button_enabled(self.button_type)
                self.check_can_gather()
            else:
                self.find_go_back_button(By.PARTIAL_LINK_TEXT, "Go Back")
                self.click_button("exit")

        except:
            raise

        # After done remove item from dict
        self.button.pop(self.button_type)

    def check_can_gather(self):

        try:
            self.can_gather = 'gather' in self.button.get(self.button_type).text
        except:
            raise