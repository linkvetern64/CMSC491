# @author Joshua Standiford, Daniel Kelly, Malik Jackson
# @description
# This file is the main file to be ran for the data analytics.
# Once the data is finished processing and running the web-interface
# will be called and the data will be loaded.

#Imports
import webbrowser
from WebLoader import open_url

def main():
    url = "crime-data.dev"

    #Register chrome web-browser
    open_url(url, 'chrome')

if __name__ == "__main__":
    main()