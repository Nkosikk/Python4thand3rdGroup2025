import time

import allure
import pytest
from allure_commons.types import AttachmentType

from Pages.homePage import HomePage
from Pages.signUpPage import  SignUpPage
from Pages.loginPage import LoginPage
from utils.readProperties_data import ReadConfig_data

class Test_RegistrationToNdosi:
    dev_url = ReadConfig_data().getURLS()
    firstname = ReadConfig_data().getFirstName()
    lastname = ReadConfig_data().getLastName()
    email = ReadConfig_data().getEmail()
    password = ReadConfig_data().getRegistrationPassword()
    confirmpassword = ReadConfig_data().getConfirmRegistrationPassword()

    @pytest.mark.dev
    def test_RegistrationToNdosiWebsite(self, setup):
        self.driver = setup
        self.driver.get(self.dev_url)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.lp = LoginPage(self.driver)
        self.sup = SignUpPage(self.driver)


        self.hp.verifyNdosiHeading()
        self.hp.clickLearningMaterial()

        self.lp.clickSignUpLink()

        self.sup.verifyNdosiSignUpPageHeading()
        allure.attach(self.driver.get_screenshot_as_png(), name="Empty Registration Page", attachment_type=AttachmentType.PNG)

        self.sup.enterFirstName(self.firstname)
        self.sup.enterLastName(self.lastname)
        self.sup.enterEmail(self.email)
        self.sup.enterPassword(self.password)
        self.sup.enterConfirmPassword(self.confirmpassword)

        allure.attach(self.driver.get_screenshot_as_png(), name="Completed Registration Page", attachment_type=AttachmentType.PNG)
        self.sup.clickCreateAccountButton()

        self.sup.acceptPopUp()
        time.sleep(10)
        allure.attach(self.driver.get_screenshot_as_png(), name="Confirmation of Account", attachment_type=AttachmentType.PNG)

        self.driver.quit()
