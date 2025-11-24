from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:
    lbl_Heading_id = "overview-hero"
    btn_learningMaterial_id = "nav-btn-practice"

    def __init__(self, driver):
        self.driver = driver

    def verifyNdosiHeading(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.ID, self.lbl_Heading_id)))
        element.is_displayed()

    def clickLearningMaterial(self):
        element = self.driver.find_element(By.ID, self.btn_learningMaterial_id)
        element.click()