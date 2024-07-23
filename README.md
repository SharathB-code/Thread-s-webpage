# Thread-s-webpage
Automation of Thread's webpage using selenium 

To run the above code, we will need to set up a few things on your machine. Here are the steps:

1. # Install Python:
   Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. # Install Required Packages:
   Install the required packages using `pip`. Open your command prompt or terminal and run the following commands:

   
  # pip install selenium
  # pip install webdriver-manager
   

3. # Microsoft Edge WebDriver:
   The `webdriver-manager` package will handle the installation of the Microsoft Edge WebDriver. However, you should ensure you have the Microsoft Edge browser installed on your system.

4. # Run the Script:
   Save the above script to a Python file, `thread.py`, and then run it using Python from your command prompt or terminal:

   
  # python thread.py
  

### Script Breakdown

1. # Imports:
   The necessary libraries are imported for the script.

2. # LoginTest Class:
   - `setUp`: This method sets up the Edge WebDriver with options to start maximized and an implicit wait of 10 seconds.
   - `test_invalid_login`: This method performs a sequence of actions to test various functionalities on the Threads website, such as invalid login, valid login, posting a thread, liking and unliking posts, following and unfollowing, and other UI interactions.
   - `tearDown`: This method closes the browser after a 10-second delay.

### Important Notes

- **XPath**: Ensure the XPaths used in the script are correct and up-to-date. If the website's structure changes, you may need to update these XPaths.
- **Website Accessibility**: The script attempts to interact with `https://www.threads.net/login`. Ensure this URL is accessible and the elements exist as expected.
- **Delays**: The script uses `time.sleep()` for delays. You may adjust these delays based on your internet speed and page load times.

### Dependencies

Here is a summary of the required dependencies:

- **Python**: Ensure you have Python 3.x installed.
- **Selenium**: Install via `pip install selenium`.
- **webdriver-manager**: Install via `pip install webdriver-manager`.
- **Microsoft Edge Browser**: Download and install from the [official site](https://www.microsoft.com/en-us/edge).

### Command to Install Dependencies

# pip install selenium webdriver-manager


After ensuring all the above steps and dependencies are in place, you should be able to run the script successfully.
