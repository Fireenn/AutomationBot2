from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

from Bot.button_click import Button


class Attack(Button):

    def __init__(self, browser: webdriver):
        super().__init__(browser)

        self.button_type: str = 'attack'
        self._opponent_hp: int = 1

    @property
    def opponent_hp(self):
        return self._opponent_hp

    @opponent_hp.setter
    def opponent_hp(self, value: str):
        try:
            self._opponent_hp = int(value)
        except:
            raise

    def execute(self):

        self.click_button(self.button_type)

        try:
            self.find_button(By.XPATH, "//button[normalize-space()='Attack']", self.button_type)

            while self.opponent_hp > 0:
                self.click_button(self.button_type)
                self.check_opponent_hp()
        except:
            raise

        try:
            self.find_go_back_button(By.PARTIAL_LINK_TEXT, "Close")
            self.click_button('exit')
        except:
            self.browser.get("https://web.simple-mmo.com/travel")

        if self.check_url('attack'):
            try:
                self.find_go_back_button(By.PARTIAL_LINK_TEXT, "Go Back")
                self.click_button('exit')
            except:
                self.browser.get("https://web.simple-mmo.com/travel")

        return

    def check_opponent_hp(self):
        self.opponent_hp = self.browser.find_element(By.ID, 'opponent-hp').text


