import unittest
from sample.api_response import fetch_users_api
from mock_fixtures import BaseTestCase

class TestFetchUsersWithSelenium(BaseTestCase):
    def test_fetch_users(self):
        # Call the function to fetch users
        users = fetch_users_api(self.driver)

        print(users)
        user_count = len(users)
        
        # Validate basic expectations
        self.assertIsNotNone(users)
        self.assertEqual(len(users), 10)

        if user_count == 10:
            self.driver.execute_script("lambda-status=passed")
        else:
            self.driver.execute_script("lambda-status=failed") 

        # Check first user structure
        first_user = users[0]
        self.assertIn('id', first_user)
        self.assertIn('name', first_user)
        self.assertIn('username', first_user)
        
        # Validate specific user properties
        self.assertEqual(first_user['id'], 1)
        self.assertEqual(first_user['name'], 'Leanne Graham')

if __name__ == '__main__':
    unittest.main(verbosity=2, buffer=True)