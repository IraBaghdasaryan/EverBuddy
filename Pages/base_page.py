from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def _find(self, locator):
        return self.driver.find_element(locator["by"], locator["value"])

    def _find_dynamic(self, locator, unique_name):
        return self.driver.find_element(locator["by"], locator["value"] + unique_name)

    def _get_text(self, locator):
        return self.driver.find_element(locator["by"], locator["value"]).text

    def _get_text_dynamic(self, locator, unique_name):
        return self._find_dynamic(locator, unique_name).text


    def _click(self, locator):
        self._find(locator).click()

    def _click_dynamic(self, locator, unique_name):
        self._find_dynamic(locator, unique_name).click()

    def _is_displayed(self, locator):
        return self._find(locator).is_displayed()


    def _type(self, locator, input_test):
        self._find(locator).send_keys(input_test)

    def _wait_for_element(self, locator):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.visibility_of_element_located((locator["by"], locator["value"])))

    def _wait_for_element_dynamic(self, locator, unique_name):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.visibility_of_element_located((locator["by"], locator["value"] + unique_name)))

    def _find_with_image(self, image,screen):
        return self.driver.find_matches(image, screen)

    def _screenshot(self, directory, file_name):
        self.driver.get_screenshot_as_base64()
        self.driver.save_screenshot(directory + file_name)