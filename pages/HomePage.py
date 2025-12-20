from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver



    def click_customer_button(self):
        self.driver.find_element(By.XPATH, "//button[@ng-click='customer()']").click()

