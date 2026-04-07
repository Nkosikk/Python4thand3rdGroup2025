import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://ndosisimplifiedautomation.vercel.app/")

driver.find_element(By.ID, "overview-hero").is_displayed()

WelcomeHeading = driver.find_element(By.XPATH, "//*[@id='overview-hero']/h2").text

if WelcomeHeading == "Learn Automation the Right Way this is Prathamesh Testing":
    print("Welcome Heading is correct")
    assert True
else:
    print("Welcome Heading is incorrect")
    assert False

driver.find_element(By.ID, "nav-btn-practice").click()
driver.find_element(By.ID,"login-email").send_keys("Tatalo.Mkhize@example.com")
driver.find_element(By.ID,"login-password").send_keys("England@123456")
driver.find_element(By.ID, "login-submit").click()
time.sleep(10)
driver.find_element(By.ID, "practice-heading").is_displayed()
time.sleep(15)

