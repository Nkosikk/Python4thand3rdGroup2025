from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:
    lbl_Heading_xpath = "//h1[@class='hero-title' and text()='Master Test Automation']"
    btn_Login_xpath = "//button[@class='user-pill' and .//span[text()='Login']]"

    def __init__(self, driver):
        self.driver = driver

    def verifyNdosiHeading(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.lbl_Heading_xpath)))
        element.is_displayed()

    def clickLoginButton(self):
        element = self.driver.find_element(By.XPATH, self.btn_Login_xpath)
        element.click()
