from selenium import webdriver

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to a URL
driver.get("https://www.wizklub.com")

# Refresh the page multiple times
for i in range(3):
    driver.refresh()
