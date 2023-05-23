import unittest
from time import sleep
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from Utilities.ReadExcel_Input import ReadExcelInput


class ConnectAndroid:
    dc = {}
    driver = None

    @pytest.fixture(autouse=True)
    def setUp(self) -> None:
        device_config = ReadExcelInput().read_device_configuration()
        self.dc['app'] = "C:\\Users\\udch0622\\Documents\\Uday-Personal\\Learnings\\PythonPrograms\\AndroidApp\\General-Store.apk"
        self.dc['platformName'] = device_config.get('PlatformName')
        self.dc['deviceName'] = device_config.get('DeviceName')
        self.dc['udid'] = device_config.get('UDID')
        self.dc['appPackage'] = device_config.get('AppPackage')
        self.dc['automationName'] = 'UiAutomator2'
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.dc)

    def tearDown(self) -> None:
        "Tear down the test"
        self.driver.quit()

    # def test_launch_GeneralStore_App(self):
    #     # Wait till App home page is launched properly
    #     sleep(5)
    #     # self.driver.implicitly_wait(5)
    #     if self.driver.find_element(by=AppiumBy.ID,
    #                                 value='com.androidsample.generalstore:id/toolbar_title').is_displayed():
    #         print("General Store App Launched Successfully")
    #     else:
    #         print("General store app was not launched after 5 seconds")
    #
    #     countryList = self.driver.find_element(by=AppiumBy.ID, value='com.androidsample.generalstore:id/spinnerCountry')
    #     countryList.click()
    #     sleep(5)
    #
    #     #  Scroll to find the desired Country Name
    #     for _ in range(25):
    #         end_y = 800
    #         try:
    #             checkCountry = self.driver.find_element(by=AppiumBy.XPATH,
    #                                                     value="//android.widget.TextView[@text='India']").is_displayed()
    #             if checkCountry is True:
    #                 self.driver.find_element(by=AppiumBy.XPATH,
    #                                          value="//android.widget.TextView[@text='India']").click()
    #                 break
    #         except:
    #             self.driver.swipe(240, 1150, 240, end_y, 250)
    #             self.driver.implicitly_wait(1)
    #             print(_)
    #             continue
    #     sleep(3)
