from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

def fetch_users_api(driver):
    """
    Fetch users from JSONPlaceholder API using Selenium
    
    Returns:
    list: List of user dictionaries
    """
    
    try:
        # Navigate to the API endpoint
        driver.get('https://jsonplaceholder.typicode.com/users')
        
        # Wait for the pre element containing JSON data
        wait = WebDriverWait(driver, 10)
        pre_element = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'pre')))
        
        # Get and parse JSON data
        users_json = pre_element.text
        users = json.loads(users_json)
        
        return users
    except Exception as e:
        print("Something went wrong:", e)
        return []
    
