import time

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

from Bot.attack import Attack
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
            'gather': [
                'Chop',
                'Mine',
                'Salvage',
                'Catch'
            ],
            'attack': ['Attack'],
            'verify': ['pesky machine'],
            'heal': ['Heal']
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

        if self.browser.current_url != self.travel_url:
            self.move_to_travel_page()

        self.find_button(By.XPATH, "//button[normalize-space()='Take a step']", 'travel')

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


        found = False
        found_key = None

        time.sleep(1)
        for key, values in self.screen_text.items():
            if not found:
                for value in values:
                    try:
                        search_string = f'//button[normalize-space()="{value}"]'
                        self.find_button(By.XPATH, search_string, key)
                        found = True
                        found_key = key
                    except:
                        try:
                            self.find_button(By.PARTIAL_LINK_TEXT, value, key)
                            found = True
                            found_key = key
                        except:
                            continue

        if found:
            character_action = None

            if found_key == 'gather':
                character_action = Gather(self.browser)
            if found_key == "attack":
                character_action = Attack(self.browser)
            if found_key == "verify":
                self.traveling = False
            if found_key == "heal":
                pass

            if not character_action:
                return

            if hasattr(character_action, "execute") and callable(character_action.execute):
                try:
                    self.click_button(found_key)
                    character_action.execute()
                except Exception as e:
                    self.button.pop(found_key)
                    self.browser.get(self.travel_url)

                self.button.pop(found_key)

                # Re-find the button
                self.find_button(By.XPATH, "//button[normalize-space()='Take a step']")

        return

