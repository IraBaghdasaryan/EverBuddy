from Locators.locators import *
from Pages.base_page import BasePage
from appium.webdriver.common.touch_action import TouchAction

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = BasePage(driver)
        self.touchActions = TouchAction(driver)


    def login_check(self):
        self.actions._wait_for_element(LoginPageLocators._username_input)
        #self.actions._is_displayed(LoginPageLocators._username_input)

    def with_(self, username, password):
        self.actions._type(LoginPageLocators._username_input, username)
        self.actions._type(LoginPageLocators._password_input, password)
        self.actions._click(LoginPageLocators._enter_button)




