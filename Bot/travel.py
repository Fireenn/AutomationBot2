import time

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

from Bot.button_click import Button
from Bot.gather import Gather


class Travel(Button):

    def __init__(self, browser: webdriver):
        super().__init__(browser)

        self.travel_url = "https://web.simple-mmo.com/travel"
        self._traveling = False

        # During traveling things can happen that can pop up.
        # Be able to handle events on the screen
        self.screen_text = {
            'gather:': [
                'Chop',
                'Mine',
                'Salvage',
                'Catch'
            ],
            'attack': ['attack'],
            'verify': ['pesky machine'],
            'heal': ['heal']
        }

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
                # Check the screen
                # This should come last but is first due to the nature of captcha
                self.analyze_screen()
                if self.check_button_enabled():
                    self.click_button()

        except:
            # If there is an error refresh the page and set traveling to False and wait for next button click
            # Raise out and handle
            self.browser.get(self.travel_url)
            self.traveling = False
            raise

    def analyze_screen(self):

        button = None
        found = False
        found_key = None

        for key, values in self.screen_text.items():
            time.sleep(0.5)
            if not found:
                for value in values:
                    try:
                        button = self.find_button(By.PARTIAL_LINK_TEXT, value)
                        if button:
                            found = True
                            found_key = key
                    except:
                        continue

        if button and found:
            character_action = None

            if found_key == 'gather':
                character_action = Gather(self.browser)
            if found_key == "attack":
                pass
            if found_key == "verify":
                self.traveling = False
            if found_key == "heal":
                pass

            if not character_action:
                return

            if hasattr(character_action, "execute") and callable(character_action.execute):
                try:
                    character_action.execute()
                except Exception as e:
                    self.browser.get(self.travel_url)

                # Re-find the button
                self.find_button(By.XPATH, "//button[normalize-space()='Take a step']")
        return

