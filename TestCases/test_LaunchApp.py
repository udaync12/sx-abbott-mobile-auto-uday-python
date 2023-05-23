import sys
import pytest
from time import sleep
from appium.webdriver.common.appiumby import AppiumBy
from PageObject.Pages.HomePage import Home
import unittest
from appium import webdriver

from PageObject.Pages.LaunchPage import LaunchPage
from Utilities.ReadExcel_Input import ReadExcelInput


class TestGeneralStoreHomePage:
    dc = {}
    driver = None

    @pytest.fixture(autouse=True)
    def setUp(self):
        device_config = ReadExcelInput().read_device_configuration()
        self.dc[
            'app'] = "C:\\Users\\udch0622\\Documents\\Uday-Personal\\Learnings\\PythonPrograms\\AndroidApp\\General-Store.apk"
        self.dc['platformName'] = device_config.get('PlatformName')
        self.dc['deviceName'] = device_config.get('DeviceName')
        self.dc['udid'] = device_config.get('UDID')
        self.dc['appPackage'] = device_config.get('AppPackage')
        self.dc['automationName'] = 'UiAutomator2'
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.dc)

    def test_Launch_App(self, setUp):
        driver = self.driver
        driver.implicitly_wait(5)
        home = LaunchPage(driver)
        try:
            if home.get_home_page_text().is_displayed():
                print("General Store App Launched Successfully")
                # self.assert(self, True, "General Store App Launched Successfully")
                assert True
                home.get_country_drop_down().click()
                sleep(2)

                while True:
                    end_y_cord = 800
                    try:
                        if home.country_to_select().is_displayed() is True:
                            home.country_to_select().click()
                            break

                    except:
                        self.driver.swipe(240, 1150, 240, end_y_cord, 250)
                        self.driver.implicitly_wait(1)
                        continue
                    sleep(3)
    #            self.scrollToCountry(home)
        except Exception as error:
            print(error, "Failed to Load App")

    # def scrollToCountry(self, home):
    #     home.country_drop_down.click()
    #     sleep(3)
    #
    #     #  Scroll to find the desired Country Name
    #     while True:
    #         end_y_cord = 800
    #         try:
    #             checkCountry = self.driver.find_element(by=AppiumBy.XPATH,
    #                                                     value="//android.widget.TextView[@text='India']").is_displayed()
    #             if checkCountry is True:
    #                 self.driver.find_element(by=AppiumBy.XPATH,
    #                                          value="//android.widget.TextView[@text='India']").click()
    #                 break
    #         except:
    #             self.driver.swipe(240, 1150, 240, end_y_cord, 250)
    #             self.driver.implicitly_wait(1)
    #             continue
    #     sleep(3)
