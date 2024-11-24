## Python unittest.mock Guide 

Python unittest.mock module helps developers mock dependencies in their test suite. In this repository, we'll simulate the form submission process and Selenium's explicit wait (expected condition module and WebDriverWait class).

### Setup and Installation
Before you proceed, ensure that you have Python3.x and pip install on your computer.

Step 1: Clone this repository and navigate to the code directory as shown below:
```
https://github.com/ginjardev/python_unittest_mock.git
```
```
cd python_unittest_mock
```
Step 2: Create a virtual environment in your project folder with the following command on the terminal:
```
python3 -m venv venv
```
Step 3: Activate the environment:
```
source venv/bin/activate
```
Step 4: Install the dependencies from the cloned project directory:
```
pip install -r requirements.txt
```
### Authentication
Step 5: Set LambdaTest Username and Access Key in environment variables.

In order to run your tests on LambdaTest cloud platform, you will need to set your LambdaTest profile username and access key in the environment variables. Click the Access Key button at the top-right of the Automation Dashboard to access it.

See image below:

!['dashboard'](/access_key_username.png)

- Linux/mac OS
```
    export LT_USERNAME="YOUR_USERNAME" 
    export LT_ACCESS_KEY="YOUR ACCESS KEY"
```
- Windows
```
    set LT_USERNAME="YOUR_USERNAME" 
    set LT_ACCESS_KEY="YOUR ACCESS KEY"
```
### Executing The Test
Step 6: From the base repository, execute the command below in your terminal.
```
python -m unittest discover
```
Your test results would be displayed on the console (or command-line interface if you are using terminal) and on LambdaTest automation dashboard.
!['results](/results_dash.png)

