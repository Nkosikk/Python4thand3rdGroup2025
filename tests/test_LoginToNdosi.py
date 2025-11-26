import time

import allure
import pytest

from Pages.homePage import HomePage
from Pages.loginPage import LoginPage
from utils.browserSetUp import setup_Browser
from utils.readProperties_data import ReadConfig_data
from utils.commonLogin import loginToNdosi


class Test_LoginToNdosi:
    dev_url = ReadConfig_data().getURLS()
    username = ReadConfig_data().getUsername()
    password = ReadConfig_data().getPassword()

    @pytest.mark.dev
    def test_loginWithValidDetails(self, setup):
        self.driver = setup_Browser(setup)
        loginToNdosi(self.driver, self.username, self.password)
        allure.attach(self.driver.get_screenshot_as_png(), name="Learning Material Home",
                      attachment_type=allure.attachment_type.PNG)

        time.sleep(2)

        self.driver.quit()

    @pytest.mark.dev
    def test_loginWithInvalidDetails(self, setup):
        self.driver = setup_Browser(setup)
        loginToNdosi(self.driver, self.username, self.password + "invalid")
