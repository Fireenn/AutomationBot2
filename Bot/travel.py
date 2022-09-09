from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

from Bot.button_click import Button


class Travel(Button):

    def __init__(self, browser: webdriver):
        super().__init__(browser)

        self.travel_url = "https://web.simple-mmo.com/travel"
        self._traveling = False

    def __del__(self):
        pass

    @property
    def traveling(self):
        return self._traveling

    @traveling.setter
    def traveling(self, value: bool):
        self._traveling = value

    def move_to_travel_page(self):
        self.browser.get(self.travel_url)

    def begin_travel(self):

        self.traveling = True
        self.find_button(By.XPATH, "//button[normalize-space()='Take a step']")

        try:
            while self.traveling:
                if self.check_button_enabled():
                    self.click_button()

        except:
            # If there is an error refresh the page and set traveling to False and wait for next button click
            # Raise out and handle
            self.browser.get(self.travel_url)
            self.traveling = False
            raise

    def analyze_screen(self):
        pass

