from BotGUI.draw_gui import draw_login, draw_dashboard

if __name__ == '__main__':

    # return browser to be able to draw
    browser = draw_login()

    draw_dashboard(browser)

    browser.close()


