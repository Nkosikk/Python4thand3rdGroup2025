import time

import allure
import pytest
from allure_commons.types import AttachmentType

from Pages.homePage import HomePage
from Pages.loginPage import LoginPage
from Pages.learningMaterialsPage import LearningMaterialsPage
from utils.readProperties_data import ReadConfig_data
from utils.common_Login import login_to_ndosi


class Test_LoginToNdosi:
    dev_url = ReadConfig_data().getURLS()
    username = ReadConfig_data().getUsername()
    password = ReadConfig_data().getPassword()

    @pytest.mark.dev
    def test_loginToNdosiWebsite(self, setup):
        self.driver = setup
        self.driver.get(self.dev_url)
        self.driver.maximize_window()


        self.hp = HomePage(self.driver)
        self.lp = LoginPage(self.driver)
        self.lmp = LearningMaterialsPage(self.driver)


        self.hp.verifyNdosiHeading()

        self.hp.clickLearningMaterial()

        self.lp.verifyNdosiLoginPageHeading()
        allure.attach(self.driver.get_screenshot_as_png(), name="Login Page", attachment_type=AttachmentType.PNG)

        #self.lp.enterEmail(self.username)
        #self.lp.enterPassword(self.password)
        #self.lp.clickLogin()
        #self.lmp.verifyToken()

        login_to_ndosi(self.driver, self.username, self.password)

        self.lmp.verifyNdosiLearningMaterialsPageLogoutButton()
        allure.attach(self.driver.get_screenshot_as_png(), name="Learning Materials Page",attachment_type=AttachmentType.PNG)
        self.lmp.clickLogoutButton()


        self.driver.quit()
