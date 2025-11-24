import allure
from allure_commons.types import AttachmentType

from Pages.homePage import HomePage
from Pages.loginPage import LoginPage
from Pages.learningMaterialsPage import LearningMaterialsPage

def login_to_ndosi(driver, username, password):
    lp = LoginPage(driver)
    lmp = LearningMaterialsPage(driver)

    hp = HomePage(driver)
    lp = LoginPage(driver)
    lmp = LearningMaterialsPage(driver)

    hp.verifyNdosiHeading()

    hp.clickLearningMaterial()

    lp.verifyNdosiLoginPageHeading()
    allure.attach(driver.get_screenshot_as_png(), name="Login Page", attachment_type=AttachmentType.PNG)

    lp.verifyNdosiLoginPageHeading()
    lp.enterEmail(username)
    lp.enterPassword(password)
    lp.clickLogin()

