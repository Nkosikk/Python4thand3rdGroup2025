from selenium.webdriver.common.by import By


class SelectNamePage:

    def __init__(self, driver):
        self.driver = driver


    def selectNameDropDown(self):
        self.driver.find_element(By.ID, "userSelect").click()
