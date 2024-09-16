import unittest
import requests

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.frontend_url = "http://192.168.64.2:31354"

    def test_frontend_backend_integration(self):
        response = requests.get(self.frontend_url)
        
        self.assertEqual(response.status_code, 200, "Failed to access the frontend service")

        greeting_message = response.text.strip()

        expected_message = "Hello from the Backend!"

        self.assertIn(expected_message, greeting_message,"The frontend did not display the expected message from the backend")

if __name__ == '__main__':
    unittest.main()
