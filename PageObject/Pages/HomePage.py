import sys

# sys.path.append(sys.path[0] + "/...")
from appium.webdriver.common.appiumby import AppiumBy
from PageObject.Locators import Locator


class Home(object):
    def __init__(self, driver):

        self.driver = driver

        self.toolbar_title = driver.find_element(by=AppiumBy.ID, value=Locator.toolbar_title)
        self.home_page_text = driver.find_element(by=AppiumBy.XPATH, value=Locator.home_page_text)
        self.country_drop_down = driver.find_element(by=AppiumBy.ID, value=Locator.country_drop_down)
        self.country_to_select = driver.find_element(by=AppiumBy.XPATH, value=Locator.select_country)

    def get_toolbar_title(self):
        return self.toolbar_title

    def get_home_page_text(self):
        return self.home_page_text

    def get_country_drop_down(self):
        return self.country_drop_down

    def country_to_select(self):
        return self.country_to_select
