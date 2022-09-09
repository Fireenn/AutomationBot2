

# Handle login information, and to try again if login failure
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login:

    def __init__(self, browser: webdriver, username: str, password: str):
        self.browser: webdriver = browser
        self.username = username
        self.password = password

    def login(self):

        self.enter_credentials()

        pass

    def enter_credentials(self):
        email_element = self.browser.find_element(By.ID, "email")
        password_element = self.browser.find_element(By.ID, "password")

        email_element.send_keys(self.username)
        password_element.send_keys(self.password)

        self.browser.find_element(By.XPATH, '//button[normalize-space()="Sign in"]').click()
