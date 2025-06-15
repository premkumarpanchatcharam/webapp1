import unittest
from app.main import app

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_welcome_message(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to my learning world v1.0!", response.data)

if __name__ == '__main__':
    unittest.main()
# This code is a unit test for a Flask application that checks if the welcome message is served correctly.
# It uses the unittest framework to create a test case that sends a GET request to the root URL and verifies the response.
