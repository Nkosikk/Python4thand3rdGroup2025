import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.ndosiautomation.co.za/")

driver.find_element(By.ID, "overview-hero").is_displayed()

WelcomeHeading = driver.find_element(By.XPATH, "//*[@id='overview-hero']/h2").text

if WelcomeHeading == "Learn Automation the Right Way":
    print("Welcome Heading is correct")
    assert True
else:
    print("Welcome Heading is incorrect")
    assert False

driver.find_element(By.ID, "nav-btn-practice").click()

time.sleep(2)
