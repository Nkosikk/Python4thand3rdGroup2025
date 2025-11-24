import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LearningMaterialsPage:

    btn_logout_id = "logout-button"


    def __init__(self, driver):
        self.driver = driver

    def verifyNdosiLearningMaterialsPageLogoutButton(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.ID, self.btn_logout_id)))
        element.is_displayed()

    def clickLogoutButton(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.ID, self.btn_logout_id)))
        element.click()

    def verifyToken(self):
        for _ in range(20):
            token = self.driver.execute_script("return window.localStorage.getItem('authToken');")
            if token:
                print("TOKEN FOUND:", token)
                return token
            time.sleep(0.5)
        raise AssertionError("Auth token still not found after waiting!")
