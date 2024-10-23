from selenium import webdriver
from selenium.webdriver.common.by import By

def submit_form(title, description):
    driver = webdriver.Chrome()
    driver.get("https://www.lambdatest.com/selenium-playground/ajax-form-submit-demo")
    driver.find_element(By.ID, "title").send_keys(title)
    driver.find_element(By.ID, "description").send_keys(description)
    driver.find_element(By.ID, "btn-submit").click()
    return driver.title
