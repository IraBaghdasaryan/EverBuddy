import pytest
from Tests.test_base import BaseTest
from random import randrange
from Config.config import Driver
from Pages.base_page import BasePage
from Pages.welcome_page import WelcomePage
from Pages.login_page import LoginPage
from Resources import Images
from Pages.base_page import BasePage




class Test_Login(BaseTest):

    def test(self):
        driver = Driver()
        Welcome = WelcomePage(driver.driver)
        #Login = LoginPage(driver.driver)
        Welcome.click_Login()
        #assert Login.testLogincheck() == True
        #Welcome.take_screenshot()
        driver.tearDown()

LoginTest = Test_Login()

LoginTest.test()