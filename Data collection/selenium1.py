from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Configure Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")  # Add any other necessary options

# Get the path to ChromeDriver using ChromeDriverManager
chrome_driver_path = ChromeDriverManager().install()

# Create a Service object with the executable path
chrome_driver_service = Service(chrome_driver_path)

# Create a Chrome webdriver instance with the specified service and options
driver = webdriver.Chrome(service=chrome_driver_service, options=chrome_options)

# Open the Google homepage
driver.get("https://www.google.com")

# Locate the search input field using a different XPath
search_box = driver.find_element(By.XPATH, "//input[@type='text' and @name='q']")

# Input a search query
search_box.send_keys("web scraping with Selenium")

# Simulate pressing the Enter key
search_box.submit()

# Wait for a few seconds to allow the search results to load
driver.implicitly_wait(5)

# Extract search results
search_results = driver.find_elements(By.CSS_SELECTOR, "h3")

# Print the search results
for result in search_results:
    print(result.text)

# Close the web browser
driver.quit()
