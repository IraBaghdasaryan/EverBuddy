from appium import webdriver
from Config.options import desired_cap, options
import pytest

class Driver():
    def __init__(self):
        self.driver = webdriver.Remote(options["appium_url"], desired_cap)

    @pytest.fixture(autouse=True)
    def fix(self, options):
        self.options = options

    def tearDown(self):
        self.driver.quit()
