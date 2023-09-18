from ubidots import ApiClient
import requests
import time

# Ubidots API Key and Device ID
API_KEY = "YOUR_API_KEY"
DEVICE_ID = "YOUR_DEVICE_ID"

# Initialize the Ubidots client
api = ApiClient(API_KEY)

# Create a variable for online/offline status
status_variable = api.get_variable(DEVICE_ID, "online_status")

while True:
    try:
        # Check internet connectivity
        response = requests.get("https://www.google.com", timeout=10)

        # Update the online_status variable in Ubidots
        if response.status_code == 200:
            status_variable.save_value(1)  # Online
        else:
            status_variable.save_value(0)  # Offline

        time.sleep(300)  # Check status every 5 minutes
    
    except KeyboardInterrupt:
        break
