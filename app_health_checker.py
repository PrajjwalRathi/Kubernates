import requests
import time


APP_URL = "http://localhost:8080"  

# Check interval (in seconds)
CHECK_INTERVAL = 60  # Check every 60 seconds

def check_application_health(url):
    try:
        response = requests.get(url, timeout=10)  # Timeout to prevent long waits
        if 200 <= response.status_code < 300:
            print(f"Application is UP. Status code: {response.status_code}")
        else:
            print(f"Application is DOWN. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Application is DOWN. Error: {e}")

if __name__ == '__main__':
    print(f"Starting application health checker for {APP_URL}...")
    try:
        while True:
            check_application_health(APP_URL)
            time.sleep(CHECK_INTERVAL)
    except KeyboardInterrupt:
        print("\nApplication health checker stopped.")
