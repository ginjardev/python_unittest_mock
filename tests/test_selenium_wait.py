from mocks.selenium_wait import ExplicitWait
import unittest
from mock_fixtures import BaseTestCase

class TestExplicitWait(BaseTestCase):

    def test_wait_for_button_element(self):
        """Test the ExplicitWait class's ability to wait for a button element."""
        # instantiate
        explicit_wait = ExplicitWait(self.driver)

         # Call the method under test
        button_text = explicit_wait.wait_for_button_element()
        
        if button_text == 'Login':
            self.driver.execute_script("lambda-status=passed")
        else:
            self.driver.execute_script("lambda-status=failed")

        # Assertions
        self.assertEqual(button_text, "Login", "The button text should be 'Login'.")

if __name__ == "__main__":
    unittest.main()