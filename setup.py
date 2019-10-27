from selenium import webdriver
from time import sleep

class WebDriver:

    def __init__(self):
        self.browse = webdriver.Chrome(r'/Users/sanguine/Documents/Tutorials/Python_Projects/Selenium/Tutoring_Ibironke/drivers/chromedriver')

    def fetchUrl(self):

        self.browse.get("https://www.amazon.co.uk/")
        self.browse.maximize_window()

    def shutdown(self):
        sleep(5)
        self.browse.quit()

