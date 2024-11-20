from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class ExplicitWait:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.driver.get("https://ecommerce-playground.lambdatest.io/")

        # Ensure complete page load
        driver.set_page_load_timeout(10)

        self.driver.find_element(By.LINK_TEXT, "My account").click()

    def wait_for_button_element(self):
        wait = WebDriverWait(self.driver, self.timeout)
        button = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='column-right']/div/a[1]")))
        return button.text
