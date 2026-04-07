from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:
    lbl_Heading_xpath = "//h1[@class='hero-title' and text()='Master Test Automation']"
    btn_learningMaterial_xpath = "//button[@class='user-pill' and .//span[text()='Login']]"

    def __init__(self, driver):
        self.driver = driver

    def verifyNdosiHeading(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.ID, self.lbl_Heading_xpath)))
        element.is_displayed()

    def clickLearningMaterial(self):
        element = self.driver.find_element(By.ID, self.btn_learningMaterial_xpath)
        element.click()