from Locators.locators import *
from Pages.base_page import BasePage
from appium.webdriver.common.touch_action import TouchAction

class Self_meditation_Page:
    def __init__(self, driver):
        self.driver = driver
        self.actions = BasePage(driver)
        self.TouchActions = TouchAction(driver)

    def open_time_settings(self):
        self.actions._wait_for_element(SelfMeditationPageLocators._settings_button)
        self.actions._click(SelfMeditationPageLocators._settings_button)

    def close(self):
        self.actions._wait_for_element(SelfMeditationPageLocators._close_button)
        self.actions._click(SelfMeditationPageLocators._close_button)

    def start_meditation(self):
        self.actions._wait_for_element(SelfMeditationPageLocators._start_button)
        self.actions._click(SelfMeditationPageLocators._start_button)
        self.driver.implicitly_wait(3)

    def stop_meditation(self):
        self.actions._wait_for_element(SelfMeditationPageLocators._stop_button)
        self.actions._click(SelfMeditationPageLocators._stop_button)

    def set_timer_30m(self):
        self.actions._wait_for_element(SelfMeditationPageLocators._settings_button)
        self.actions._click(SelfMeditationPageLocators._settings_button)
        self.actions._wait_for_element(SelfMeditationPageLocators._time_30)
        self.actions._click(SelfMeditationPageLocators._time_30)
        self.driver.implicitly_wait(5)

    def set_timer_1h(self):
        self.actions._wait_for_element(SelfMeditationPageLocators._settings_button)
        self.actions._click(SelfMeditationPageLocators._settings_button)
        self.actions._wait_for_element(SelfMeditationPageLocators._time_1)
        self.actions._click(SelfMeditationPageLocators._time_1)
        self.driver.implicitly_wait(5)

    def set_other_time_0_5(self):
        self.actions._wait_for_element(SelfMeditationPageLocators._settings_button)
        self.actions._click(SelfMeditationPageLocators._settings_button)
        self.actions._wait_for_element(SelfMeditationPageLocators._time_other)
        self.actions._click(SelfMeditationPageLocators._time_other)
        self.actions._wait_for_element(SelfMeditationPageLocators._time_other_h)
        self.actions._click(SelfMeditationPageLocators._time_other_h)
        self.actions._wait_for_element(SelfMeditationPageLocators._one_h)
        self.actions._click(SelfMeditationPageLocators._one_h)
        self.actions._wait_for_element(SelfMeditationPageLocators._time_other_m)
        self.actions._click(SelfMeditationPageLocators._time_other_m)
        self.actions._wait_for_element(SelfMeditationPageLocators._five_m)
        self.actions._click(SelfMeditationPageLocators._five_m)
        self.driver.implicitly_wait(5)

        #self.driver.TouchActions.press(X=319, y=664).perform()
        #.actions._wait_for_element(SelfMeditationPageLocators._save_timer_button)
        #self.actions._click(SelfMeditationPageLocators._save_timer_button)
        #self.driver.implicitly_wait(5)

    def warning_close(self):
        self.actions._wait_for_element(SelfMeditationPageLocators._warning_close)
        self.actions._click(SelfMeditationPageLocators._warning_close)

    def wait_till(self, time):
        self.actions._wait_for_element_dynamic(SelfMeditationPageLocators._timer, time)
        self.actions._get_text_dynamic(SelfMeditationPageLocators._timer, time)



    def print_time(self):
        return (self.actions._get_text(SelfMeditationPageLocators._timer))

    def meditation_over(self):
        return (self.actions._get_text(SelfMeditationPageLocators._over_meditation))

    def find_image(self, screen, photo):
        return self.actions._find_with_image(screen, photo)











