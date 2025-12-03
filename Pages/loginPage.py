from selenium.webdriver.common.by import By


class LoginPage:
    lbl_loginPageHeading_id = "login-heading"
    txt_email_id = "login-email"
    txt_password_id = "login-password"
    btn_login_id = "login-submit"

    def __init__(self, driver):
        self.driver = driver

    def enterEmail(self, email):
        element = self.driver.find_element(By.ID, self.txt_email_id)
        element.send_keys(email)

    def enterPassword(self, password):
        element = self.driver.find_element(By.ID, self.txt_password_id)
        element.send_keys(password)

    def clickLoginBtn(self):
        element = self.driver.find_element(By.ID, self.btn_login_id)
        element.click()
