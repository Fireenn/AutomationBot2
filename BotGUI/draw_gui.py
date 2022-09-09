import threading

import PySimpleGUI as sg
import dotenv
from selenium.webdriver.chrome import webdriver

from Bot.browser import Browser
from Bot.login import Login

import os

from Bot.travel import Travel


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
        [sg.Checkbox('Save Credentials', key="save_credentials")],
        [sg.Button("Ok")],
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

    window = sg.Window("Dashboard", layout, size=(300, 300))

    while True:

        event, value = window.read()
        if event == sg.WIN_CLOSED:
            break

        if event == 'Travel':
            window.close()

            travel = Travel(browser)
            travel.move_to_travel_page()
            draw_travel_dashboard(browser, travel)

    window.close()


def draw_travel_dashboard(browser: webdriver, travel: Travel):

    layout = [
        [sg.Button('Automate'), sg.Button('Stop')],
    ]

    window = sg.Window("Travel", layout, size=(300, 300))

    thread = None

    while True:
        event, value = window.read()

        if event == sg.WIN_CLOSED:
            break

        if event == "Automate":
            thread = threading.Thread(target=travel.begin_travel, daemon=True)
            thread.start()
        if event == "Stop":
            travel.traveling = False

    travel.__del__()
    window.close()

    draw_dashboard(browser)
