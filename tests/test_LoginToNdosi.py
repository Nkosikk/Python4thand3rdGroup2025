import time

import allure
import pytest
from allure_commons.types import AttachmentType

from Pages.learningMaterialsPage import LearningMaterialsPage
from Pages.loginPage import LoginPage
from utils.readProperties_data import ReadConfig_data
from utils.common_Login import login_to_ndosi
from utils.browserSetup import setup_browser


class Test_LoginToNdosi:
    dev_url = ReadConfig_data().getURLS()
    username = ReadConfig_data().getUsername()
    password = ReadConfig_data().getPassword()

    @pytest.mark.dev
    def test_loginToNdosiWebsiteWithValidCredentials(self, setup):
        self.driver = setup_browser(setup)
        self.lmp = LearningMaterialsPage(self.driver)

        login_to_ndosi(self.driver, self.username, self.password)

        self.lmp.verifyToken()

        self.lmp.verifyNdosiLearningMaterialsPageLogoutButton()
        allure.attach(self.driver.get_screenshot_as_png(), name="Learning Materials Page",attachment_type=AttachmentType.PNG)
        self.lmp.clickLogoutButton()

        self.driver.quit()

    @pytest.mark.dev
    def test_loginToNdosiWebsiteWithInvalidCredentials(self, setup):
        self.driver = setup_browser(setup)

        self.lp = LoginPage(self.driver)

        login_to_ndosi(self.driver, self.username, self.password+"wrong")

        self.lp.acceptPopUp()

        allure.attach(self.driver.get_screenshot_as_png(), name="Login Screen Error",attachment_type=AttachmentType.PNG)

        self.driver.quit()
