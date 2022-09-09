from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Browser:

    def __init__(self):
        self._browser = None

    @property
    def browser(self):
        return self._browser

    @browser.setter
    def browser(self, value: webdriver):
        self._browser = value

    def open_browser(self):

        opts = Options()
        opts.add_experimental_option("detach", True)

        browser = webdriver.Chrome(chrome_options=opts)
        # browser.maximize_window()
        browser.get('https://web.simple-mmo.com/login')
        self.browser = browser

    def close(self):
        self.browser.close()
