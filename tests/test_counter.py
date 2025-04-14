# tests/test_counter.py


from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
def test_increment_button():
    # Create a new Chrome browser instance
    driver = webdriver.Chrome()

    try:
        # Open the local web app
        driver.get("http://localhost:3000/index.html")

        # Find the counter element
        counter = driver.find_element(By.ID, "counter")
        increment_button = driver.find_element(By.ID, "increment")

        # Click the increment button
        increment_button.click()
        time.sleep(1)  # wait for DOM update

        # Check if the counter shows '1'
        assert counter.text == "1", f"Expected counter to be 1, got {counter.text}"

    finally:
        driver.quit()


# This is a test that checks if the counter can go below 0 (which it should NOT)
def test_counter_cannot_be_negative():
    # Launch a new Chrome browser window
    driver = webdriver.Chrome()

    try:
        # Open the local page with the counter
        driver.get("http://localhost:3000/index.html")

        # Find the element that displays the counter value
        counter = driver.find_element(By.ID, "counter")

        # Find the decrement button by its ID
        decrement_button = driver.find_element(By.ID, "decrement")

        # Click the decrement button 3 times (even if it's already at 0)
        for _ in range(3):
            decrement_button.click()
            time.sleep(0.5)  # wait a little after each click, to simulate user behavior

        # Read the current value of the counter and make sure it's not less than 0
        # If it is, the test will fail and show an error with the actual value
        assert int(counter.text) >= 0, f"Counter went below 0: {counter.text}"

    finally:
        # Close the browser window, even if test fails
        driver.quit()