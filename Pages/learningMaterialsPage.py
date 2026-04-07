import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LearningMaterialsPage:
    btn_pill_xpath = "//button[contains(@class,'user-pill') and .//span[text()='👤']]"
    btn_logout_xpath = "//button[contains(@class,'nav-dropdown-item') and .//span[normalize-space()='Logout']]"


    def __init__(self, driver):
        self.driver = driver

    def verifyNdosiLogoutButton(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.btn_pill_xpath)))
        element.is_displayed()

    def clickLogoutDropdown(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH,self.btn_pill_xpath)))
        element.click()

    def clickLogoutButton(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.btn_logout_xpath)))
        element.click()

    def verifyToken(self):
        for _ in range(20):
            token = self.driver.execute_script("return window.localStorage.getItem('authToken');")
            if token:
                print("TOKEN FOUND:", token)
                return token
            time.sleep(0.5)
        raise AssertionError("Auth token still not found after waiting!")
