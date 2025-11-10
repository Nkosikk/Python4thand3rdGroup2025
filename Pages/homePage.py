from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    lbl_Heading_id = "overview-hero"

    def __init__(self, driver):
        self.driver = driver

    def verifyNdosiHeading(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.ID, self.lbl_Heading_id)))
        element.is_displayed()
