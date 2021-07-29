from Tests.test_base import BaseTest
from Config.config import Driver
from Pages import home_page, self_meditation_page
import pytest
import time

class Test_Self_Meditation(BaseTest):

    def test_30m(self):
        driver = Driver()
        home = home_page.HomePage(driver.driver)
        self_meditation = self_meditation_page.Self_meditation_Page(driver.driver)

        home.go_to_self_meditation()
        self_meditation.set_timer_30m()
        check_time = self_meditation.print_time()
        print (check_time)

        assert check_time == "30:00"

    def test_1h(self):
        driver = Driver()
        home = home_page.HomePage(driver.driver)
        self_meditation = self_meditation_page.Self_meditation_Page(driver.driver)

        home.go_to_self_meditation()
        self_meditation.set_timer_1h()
        time.sleep(3)
        check_time = self_meditation.print_time()
        print(check_time)

        assert check_time == "01:00"

    def test_other_time(self):
        driver = Driver()
        home = home_page.HomePage(driver.driver)
        self_meditation = self_meditation_page.Self_meditation_Page(driver.driver)

        home.go_to_self_meditation()
        self_meditation.set_other_time_0_5()
        check_time = self_meditation.print_time()

        assert check_time == "05:00"

    def test_over(self):
        driver = Driver()
        home = home_page.HomePage(driver.driver)
        self_meditation = self_meditation_page.Self_meditation_Page(driver.driver)

        home.go_to_self_meditation()
        self_meditation.start_meditation()
        #time.sleep(3)
        #self_meditation.wait_till("29:57")
        self_meditation.stop_meditation()
        self_meditation.warning_close()
        over = self_meditation.meditation_over()
        print(over)







test_meditation = Test_Self_Meditation()
#test_meditation.test_30m()
#test_meditation.test_1h()
#test_meditation.test_other_time()
test_meditation.test_over()