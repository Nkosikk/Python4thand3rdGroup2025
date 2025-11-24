from Pages.homePage import HomePage
from Pages.loginPage import LoginPage

def loginToNdosi(driver,username,password):
    hp = HomePage(driver)
    hp.verifyNdosiHeading()
    hp.clickLearningMaterial()
    login=LoginPage(driver)
    login.enterEmail(username)
    login.enterPassword(password)
    login.clickLoginBtn()


