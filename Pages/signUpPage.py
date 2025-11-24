import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignUpPage:
    lbl_Heading_id = "registration-heading"
    txt_FirstNameField_id = "register-firstName"
    txt_LastNameField_id = "register-lastName"
    txt_EmailField_xpath = "//input[@placeholder='Email']"
    txt_PasswordField_xpath = "//input[@placeholder='Password']"
    txt_ConfirmPasswordField_xpath = "//input[@placeholder='Confirm Password']"
    btn_CreateAccount_xpath = "//button[contains(text(),'Create Account')]"

    def __init__(self, driver):
        self.driver = driver

    def verifyNdosiSignUpPageHeading(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.ID, self.lbl_Heading_id)))
        assert element.is_displayed()

    def enterFirstName(self,firstname):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.ID, self.txt_FirstNameField_id)))
        element.send_keys(firstname)

    def enterLastName(self,lastname):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.ID, self.txt_LastNameField_id)))
        element.send_keys(lastname)

    def enterEmail(self,email):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.txt_EmailField_xpath)))
        element.send_keys(email)

    def enterPassword(self,password):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.txt_PasswordField_xpath)))
        element.send_keys(password)

    def enterConfirmPassword(self,confirmpassword):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.txt_ConfirmPasswordField_xpath)))
        element.send_keys(confirmpassword)

    def clickCreateAccountButton(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.btn_CreateAccount_xpath)))
        element.click()

    def acceptPopUp(self):
        wait = WebDriverWait(self.driver, 10)
        alert = wait.until(EC.alert_is_present())

        expected_message = "Registration successful! You can now login with your credentials."
        actual_message = alert.text

        assert actual_message == expected_message, \
            f"Unexpected alert text! Expected: '{expected_message}' but got: '{actual_message}'"

        alert.accept()

    