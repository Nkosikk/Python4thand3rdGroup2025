import time

import pytest

from Pages.homePage import HomePage
from Pages.loginPage import LoginPage
from utils.readProperties_data import ReadConfig_data


class Test_LoginToNdosi:
    dev_url = ReadConfig_data().getURLS()
    username = ReadConfig_data().getUsername()
    password = ReadConfig_data().getPassword()

    @pytest.mark.dev
    def test_loginWithValidDetails(self, setup):
        self.driver = setup
        self.driver.get(self.dev_url)
        self.driver.maximize_window()
        self.hp = HomePage(self.driver)
        self.hp.verifyNdosiHeading()
        self.hp.clickLearningMaterial()
        self.login=LoginPage(self.driver)
        self.login.enterEmail(self.username)
        self.login.enterPassword(self.password)
        self.login.clickLoginBtn()

        time.sleep(2)

        self.driver.quit()
    @pytest.mark.dev
    def test_loginWithInvalidDetails(self, setup):
        self.driver = setup
        self.driver.get(self.dev_url)
        self.driver.maximize_window()
        self.hp = HomePage(self.driver)
        self.hp.verifyNdosiHeading()
        self.hp.clickLearningMaterial()
        self.login = LoginPage(self.driver)
        self.login.enterEmail(self.username)
        self.login.enterPassword(self.password+"invalid")
        self.login.clickLoginBtn()


