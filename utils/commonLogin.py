from Pages.homePage import HomePage
from Pages.loginPage import LoginPage
from tests.conftest import setup
from utils.readProperties_data import ReadConfig_data




def loginToNdosi(driver,username,password):

    hp = HomePage(driver)
    hp.verifyNdosiHeading()
    hp.clickLearningMaterial()
    login=LoginPage(driver)
    login.enterEmail(username)
    login.enterPassword(password)
    login.clickLoginBtn()



