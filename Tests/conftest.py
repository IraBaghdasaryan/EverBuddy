import pytest
from selenium import webdriver
from Config.options import desired_cap, options



class Driver():
    def __init__(self):
        self.driver = webdriver.Remote(options["appium_url"], desired_cap)

    # def __del__(self):
    # self.driver.quit()

    def tearDown(self):
        self.driver.quit()