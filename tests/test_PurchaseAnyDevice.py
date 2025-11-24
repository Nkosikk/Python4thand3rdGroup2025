import allure
import pytest
from allure_commons.types import AttachmentType

from Pages.homePage import HomePage
from Pages.learningMaterialsPage import LearningMaterialsPage
from Pages.loginPage import LoginPage
from utils.readProperties_data import ReadConfig_data


class Test_PurchaseAnyDevice:
    dev_url = ReadConfig_data().getURLS()
    username = ReadConfig_data().getUsername()
    password = ReadConfig_data().getPassword()

    @pytest.mark.dev
    def test_DevicePurchase(self, setup):
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

        self.lp.enterEmail(self.username)
        self.lp.enterPassword(self.password)
        self.lp.clickLogin()


        self.driver.quit()





