from Locators.locators import *
from Pages.base_page import BasePage
from appium.webdriver.common.touch_action import TouchAction

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = BasePage(driver)
        self.touchActions = TouchAction(driver)

    def go_to_learning(self):
        self.actions._wait_for_element(HomePageLocators._learning_button)
        self.actions._click(HomePageLocators._learning_button)
        self.actions._screenshot(r"C:\Users\Admin\PycharmProjects\EverBuddy\Resources\Images", 'newscreen.png')



    def go_to_self_meditation(self):
        self.actions._wait_for_element(HomePageLocators._self_meditation_button)
        self.actions._click(HomePageLocators._self_meditation_button)



    def go_to_settings(self):
        self.actions._wait_for_element(HomePageLocators._settings_button)
        self.actions._click(HomePageLocators._settings_button)

