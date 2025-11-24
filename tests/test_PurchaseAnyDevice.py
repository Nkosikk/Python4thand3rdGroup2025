import allure
import pytest
from allure_commons.types import AttachmentType

from Pages.homePage import HomePage
from Pages.learningMaterialsPage import LearningMaterialsPage
from Pages.loginPage import LoginPage
from utils.browserSetup import setup_browser
from utils.common_Login import login_to_ndosi
from utils.readProperties_data import ReadConfig_data


class Test_PurchaseAnyDevice:
    dev_url = ReadConfig_data().getURLS()
    username = ReadConfig_data().getUsername()
    password = ReadConfig_data().getPassword()

    @pytest.mark.dev
    def test_DevicePurchase(self, setup):

        self.driver = setup_browser(setup)

        login_to_ndosi(self.driver, self.username, self.password)

        self.driver.quit()





