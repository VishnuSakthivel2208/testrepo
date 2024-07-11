from appium import webdriver

# Define desired capabilities
desired_caps = {
    "platformName": "tizentv",
    "appium:automationName": "tizentv",
    "appium:deviceName": "0BRW3CARC00856M",
    "appium:udid": "0BRW3CARC00856M",
    "headspin:app.id": "93a2670b-9fc7-4286-802d-151d54b10d59"
}

# Define Grid URL
grid_url = "https://dev-us-pao-20.headspin.io:7301/v0/a656c95ebb63490a9e8f6f095053e565/wd/hub"

# Initialize the driver
driver = webdriver.Remote(grid_url, desired_caps)

# Perform actions with the driver...
# For example, driver.get("https://example.com")

# Quit the driver session when done
driver.quit()

