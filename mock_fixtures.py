import os
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

username = os.getenv("LT_USERNAME") 
access_key = os.getenv("LT_ACCESS_KEY") 

options = ChromeOptions()
options.browser_version = "129"
options.platform_name = "Windows 10"
lt_options = {}
lt_options["username"] = username
lt_options["accessKey"] = access_key
lt_options["build"] = "Python Mock Build"
lt_options["project"] = "Untitled 1"
lt_options["name"] = "Python Unittest Mock"
lt_options["w3c"] = True
lt_options["plugin"] = "python-python"
options.set_capability('LT:Options', lt_options)


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        """This method is called before each test."""
        self.driver = webdriver.Remote(
            command_executor="http://{}:{}@hub.lambdatest.com/wd/hub".format(
                username, access_key
            ),
            options=options,
        )

    def tearDown(self):
        """This method is called after each test."""
        self.driver.quit()  # Clean up and close the browser



if __name__ == "__main__":
    unittest.main()
