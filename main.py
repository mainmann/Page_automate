from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver (ensure ChromeDriver is installed and in PATH)
driver = webdriver.Chrome()

# Navigate to the LMS login page
driver.get("https://vulms.vu.edu.pk/Login.aspx")

# Log in to the LMS (replace with your credentials)
username = driver.find_element_by_id("txtStudentID")  # Adjust ID if different
password = driver.find_element_by_id("txtPassword")  # Adjust ID if different
username.send_keys("your_student_id")
password.send_keys("your_password")
login_button = driver.find_element_by_id("btnLogin")  # Adjust ID if different
login_button.click()

# Wait for the dashboard to load (adjust locator as needed)
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "some_dashboard_element")))

# Navigate to the lecture page (replace with your actual lecture URL)
driver.get("https://vulms.vu.edu.pk/Courses/CS101/Lectures/Lecture1.aspx")

# Locate the iframe with the YouTube video
iframe = driver.find_element_by_css_selector("iframe[src*='youtube.com']")
driver.switch_to.frame(iframe)

# Find the video element
video = driver.find_element_by_tag_name("video")

# Get the video duration
duration = driver.execute_script("return arguments[0].duration", video)

# Ensure the video is playing
driver.execute_script("if (arguments[0].paused) { arguments[0].play(); }", video)

# Monitor video playback
alerted = False
while True:
    current_time = driver.execute_script("return arguments[0].currentTime", video)
    if current_time >= duration:
        break
    if current_time >= 0.25 * duration and not alerted:
        print("25% of the video has been watched.")
        alerted = True
    time.sleep(5)  # Check every 5 seconds

# Switch back to the main content
driver.switch_to.default_content()

# Switch to the next tab (e.g., Quiz tab)
quiz_tab = driver.find_element_by_xpath("//a[contains(text(), 'Quiz')]")  # Adjust locator if needed
quiz_tab.click()


driver.quit()