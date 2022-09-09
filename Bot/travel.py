from selenium.webdriver.chrome import webdriver

from Bot.button_click import Button


class Travel(Button):

    def __init__(self, browser: webdriver):
        super().__init__(browser)

        self.travel_url = "https://web.simple-mmo.com/travel"
        self._traveling = False

    @property
    def traveling(self):
        return self._traveling

    @traveling.setter
    def traveling(self, value: bool):
        self._traveling = value

    def move_to_travel_page(self):
        self.browser.get(self.travel_url)

    def begin_travel(self):
        pass
