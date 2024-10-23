import unittest
from unittest.mock import patch, MagicMock
from mocks.mock_submit_form import submit_form
from selenium.webdriver.common.by import By
from mock_fixtures import BaseTestCase

class TestSubmitFormFunction(BaseTestCase):
    @patch('run_tests.webdriver.Remote')  # Patch Remote WebDriver
    def test_submit_form(self, mock_webdriver):
        # Create a mock WebDriver instance
        mock_driver = MagicMock()
        mock_webdriver.return_value = mock_driver
        
        # Mock find_element and get to prevent opening a real browser
        mock_driver.find_element.return_value = MagicMock()
        mock_driver.get.return_value = None
        mock_driver.title = "Selenium Grid Online | Run Selenium Test On Cloud"

        # Call the function with test inputs
        title = submit_form(mock_driver,"home", "homepage")

        if title:
            self.driver.execute_script("lambda-status=passed")
        else:
            self.driver.execute_script("lambda-status=failed")

        # # Assert that the correct elements were interacted with
        mock_driver.find_element.assert_any_call(By.ID, "title")
        mock_driver.find_element.assert_any_call(By.ID, "description")
        mock_driver.find_element.assert_any_call(By.ID, "btn-submit")

        # Assert that the driver navigated to the correct page
        mock_driver.get.assert_called_once_with("https://www.lambdatest.com/selenium-playground/ajax-form-submit-demo")

        # Assert the final page title is "Dashboard"
        self.assertEqual(title, "Selenium Grid Online | Run Selenium Test On Cloud")

if __name__ == '__main__':
    unittest.main()
