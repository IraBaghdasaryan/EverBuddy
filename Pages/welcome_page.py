from Locators.locators import *
from Pages.base_page import BasePage
from appium.webdriver.common.touch_action import TouchAction

class WelcomePage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = BasePage(driver)
        self.touchActions = TouchAction(driver)

    def click_Login(self):
        self.actions._wait_for_element(WelcomePageLocators._login_button)
        self.actions._click(WelcomePageLocators._login_button)
        self.driver.implicitly_wait(30)

    def click_Registration(self):
        self.actions._wait_for_element(WelcomePageLocators._registration_button)
        self.actions._click(WelcomePageLocators._registration_button)
        self.driver.implicitly_wait(5)

    def click_Google(self):
        self.actions._wait_for_element(WelcomePageLocators._google_button)
        self.actions._click(WelcomePageLocators._google_button)

    def click_vk(self):
        self.actions._wait_for_element(WelcomePageLocators._vk_button)
        self.actions._click(WelcomePageLocators._vk_button)

    def click_fb(self):
        self.actions._wait_for_element(WelcomePageLocators._fb_button)
        self.actions._click(WelcomePageLocators._fb_button)


