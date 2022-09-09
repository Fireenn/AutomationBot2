import PySimpleGUI as sg
import dotenv
from selenium.webdriver.chrome import webdriver

from Bot.browser import Browser
from Bot.login import Login

import os


def save_login_credentials(username, password):

    dotenv_file = dotenv.find_dotenv()
    dotenv.load_dotenv(dotenv_file)

    os.environ['login_username'] = username
    dotenv.set_key(dotenv_file, "login_username", os.environ['login_username'])

    os.environ['login_password'] = password
    dotenv.set_key(dotenv_file, "login_password", os.environ['login_password'])


def draw_login() -> webdriver:

    dotenv_file = dotenv.find_dotenv()
    dotenv.load_dotenv(dotenv_file)

    layout = [
        [sg.Text("Username", size=(15, 1)), sg.InputText(key='username', font=16, default_text=os.environ.get('login_username'))],
        [sg.Text("Password", size=(15, 1)), sg.InputText(key='password', font=16,password_char='*', default_text=os.environ.get('login_password'))],
        [sg.Button("Ok")],
        [sg.Checkbox('Save Credentials', key="save_credentials")]
    ]

    window = sg.Window('Login Info', layout)

    while True:

        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        if event == 'Ok':
            if values.get('save_credentials'):
                save_login_credentials(values.get('username'), values.get('password'))

            break

    window.close()

    chrome = Browser()
    chrome.open_browser()

    data = {
        'browser': chrome.browser,
        'username': values.get('username'),
        'password': values.get('password'),
    }

    login = Login(**data)
    try:
        login.login()
    except Exception as e:
        print(e.__str__())
        chrome.close()

    return chrome.browser


def draw_dashboard(browser: webdriver):

    layout = [
        [sg.Button("Travel")],
    ]

    window = sg.Window("Dashboard", layout)

    while True:

        event, value = window.read()
        if event == sg.WIN_CLOSED:
            break

        if event == 'Travel':
            print("In")

        print(event)

    window.close()