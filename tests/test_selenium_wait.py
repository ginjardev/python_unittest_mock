import unittest
from unittest.mock import patch, MagicMock
from mocks.mock_selenium_wait import ExplicitWait
from selenium.webdriver.common.by import By
from run_tests import BaseTestCase


class TestWaitForElement(BaseTestCase):
    @patch('mocks.mock_selenium_wait.WebDriverWait')
    @patch('mocks.mock_selenium_wait.EC.visibility_of_element_located')
    def test_wait_for_button_element(self, mock_visibility_of_element_located, mock_WebDriverWait):
        # Create a mock WebDriver instance
        mock_driver = MagicMock()
        
        # Mock the condition to return a mocked element
        mock_element = MagicMock()
        mock_element.text = "Login"
        mock_visibility_of_element_located.return_value = mock_element
        
        # Mock the wait instance to return the condition
        mock_wait_instance = MagicMock()
        mock_wait_instance.until.return_value = mock_element
        mock_WebDriverWait.return_value = mock_wait_instance

        # Call the function
        explicit_wait = ExplicitWait(mock_driver)
        result = explicit_wait.wait_for_button_element()


        # Assert that WebDriverWait was called correctly
        mock_WebDriverWait.assert_called_once_with(mock_driver, 10)

        # Assert that visibility_of_element_located was called with the correct locator
        mock_visibility_of_element_located.assert_called_once_with((By.XPATH, "//input[@type='submit']"))

        if result:
            self.driver.execute_script("lambda-status=passed")
        else:
            self.driver.execute_script("lambda-status=failed")

        # Assert the returned text is as expected
        self.assertEqual(result, "Login")

if __name__ == '__main__':
    unittest.main()
