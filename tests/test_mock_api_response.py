import unittest
from unittest.mock import MagicMock, patch
from mock_fixtures import BaseTestCase
from sample.api_response import fetch_users_api

class TestFetchUsersAPI(BaseTestCase):
    @patch('sample.api_response.WebDriverWait') 
    @patch('sample.api_response.By')
    def test_fetch_users_api(self, mock_by, mock_webdriver_wait):
        # Create a mock driver
        mock_driver = MagicMock()

        # Create a mock element to simulate the 'pre' element containing JSON data
        mock_pre_element = MagicMock()
        mock_pre_element.text = '[{"id": 1, "name": "John Doe"}, {"id": 2, "name": "Jane Smith"}]'
        
        # Set up the mock for WebDriverWait and its return value
        mock_wait_instance = MagicMock()
        mock_wait_instance.until.return_value = mock_pre_element
        mock_webdriver_wait.return_value = mock_wait_instance
        
        # Call the function under test
        users = fetch_users_api(mock_driver)
        
        # Assert that the returned users match the expected result
        expected_users = [{"id": 1, "name": "John Doe"}, {"id": 2, "name": "Jane Smith"}]
        self.assertEqual(users, expected_users)

        if len(users) > 0:
            self.driver.execute_script("lambda-status=passed")
        else:
            self.driver.execute_script("lambda-status=failed")

        # Verify that driver.get was called with the correct URL
        mock_driver.get.assert_called_once_with('https://jsonplaceholder.typicode.com/users')
        
        # Verify that WebDriverWait was called correctly
        mock_webdriver_wait.assert_called_once_with(mock_driver, 10)

if __name__ == '__main__':
    unittest.main(verbosity=2)