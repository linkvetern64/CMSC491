# @author Joshua Standiford, Daniel Kelly, Malik Jackson
# @description
# This file is the controller for loading the web interface
#

import os, platform, webbrowser

#do by OS and by path
#Returns web controller for chosen browser to load
#Parameters: ID - String - intended browser, or default if empty
def register_browsers(ID):

    OS = platform.system()

    #If system is windows, install webbrowser paths and return selected controller
    if(OS == "Windows"):
        CHROME_PATH = "C:\\Program Files (x86)\\Google\\Chrome\\Application\chrome.exe"
        FIREFOX_PATH = "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"
        if ID == 'chrome':
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(CHROME_PATH), 1)
            return webbrowser.get('chrome')

        elif ID == 'firefox':
            webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(FIREFOX_PATH), 1)
            return webbrowser.get('firefox')

        else:
            #If you can't find or recognize either ID, return default browser
            return webbrowser.get()

    #Current Linux support returns default browser
    elif(OS == "Linux"):
        return webbrowser.get()

    return None

#Browser parameter should be
# 'chrome'
# 'firefox'
def open_url(url, browser):
    controller = register_browsers(browser)
    controller.open(url, 2, True)