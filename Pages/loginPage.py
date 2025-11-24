from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    lbl_Heading_xpath = "//h2[contains(., 'Login to') and contains(., 'Access Learning Materials')]"
    txt_EmailField_id = "login-email"
    txt_PasswordField_id ="login-password"
    btn_Login_id = "login-submit"
    lnk_SignUpLink_id ="signup-toggle"

    def __init__(self, driver):
        self.driver = driver

    def verifyNdosiLoginPageHeading(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.lbl_Heading_xpath)))
        element.is_displayed()

    def enterEmail(self,username):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.ID, self.txt_EmailField_id)))
        element.send_keys(username)

    def enterPassword(self,password):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.ID, self.txt_PasswordField_id)))
        element.send_keys(password)

    def clickLogin(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.ID, self.btn_Login_id)))
        element.click()

    def clickSignUpLink(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.ID, self.lnk_SignUpLink_id)))
        element.click()

    def acceptPopUp(self):
        wait = WebDriverWait(self.driver, 10)
        alert = wait.until(EC.alert_is_present())

        expected_message = "Invalid email or password"
        actual_message = alert.text

        assert actual_message == expected_message, \
            f"Unexpected alert text! Expected: '{expected_message}' but got: '{actual_message}'"

        alert.accept()