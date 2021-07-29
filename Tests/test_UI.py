from Pages.base_page import BasePage
from Tests.test_base import BaseTest
from Config.config import Driver
from Pages import home_page, self_meditation_page, base_page
import pytest
import time

class Test_Image(BaseTest):


    def test_UI(self):
        driver = Driver()
        home = home_page.HomePage(driver.driver)
        self_meditation = self_meditation_page.Self_meditation_Page(driver.driver)
        base = base_page.BasePage(driver.driver)


        home.go_to_self_meditation()
        self_meditation.set_other_time_0_5()
        screen =base._screenshot(r"C:\Users\Admin\PycharmProjects\EverBuddy\Resources\Images", 'newnewscreen.png')
        self_meditation.find_image(screen, r"C:\Users\Admin\PycharmProjects\EverBuddy\Resources\Check\Screenshot_1626343691.png", )


        #self_meditation.set_other_time_0_5()
        #self.driver.update_settings({"getMatchedImageResult": True})
        #el = self.driver.find_element_by_image('')
        #el.get_attribute('visual')


        #assert check_time == "05:00"


test_Ui = Test_Image()
test_Ui.test_UI()