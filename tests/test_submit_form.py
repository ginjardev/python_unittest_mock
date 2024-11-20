from mock_fixtures import BaseTestCase
from mocks.submit_form import submit_form
import unittest


class TestSubmitForm(BaseTestCase):

    def test_submit_form(self):
        """Test the submit_form function with valid inputs."""
        title = "Test Title"
        description = "This is a test description."

        # Call the function under test
        page_title = submit_form(self.driver, title, description)

        if page_title:
            self.driver.execute_script("lambda-status=passed")
        else:
            self.driver.execute_script("lambda-status=failed")       

        # Assertions
        self.assertEqual(page_title, "Selenium Grid Online | Run Selenium Test On Cloud")

if __name__ == "__main__":
    unittest.main()