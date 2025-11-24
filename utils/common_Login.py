
from Pages.loginPage import LoginPage
from Pages.learningMaterialsPage import LearningMaterialsPage

def login_to_ndosi(driver, username, password):
    lp = LoginPage(driver)
    lmp = LearningMaterialsPage(driver)

    lp.verifyNdosiLoginPageHeading()
    lp.enterEmail(username)
    lp.enterPassword(password)
    lp.clickLogin()
    lmp.verifyToken()
