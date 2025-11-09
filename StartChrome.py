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
driver.find_element(By.ID, "login-email").send_keys("JohnDoe@gmail.com")
driver.find_element(By.ID, "login-password").send_keys("John@1234")
driver.find_element(By.ID, "login-submit").click()
time.sleep(3)
driver.find_element(By.ID,"tab-btn-password").click()
driver.find_element(By.ID,"name").send_keys(" John Doe")
driver.find_element(By.ID,"email").send_keys("Johndoe@gmail.com")
driver.find_element(By.ID,"age").send_keys(1)

time.sleep(2)
