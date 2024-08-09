import unittest
from unittest.mock import patch

from main import app, server_status_global

class FlaskAppTests(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        
    def test_index_get(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Status', response.data)
        
    def test_get_server_status(self):
        response = self.app.get('/status')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, server_status_global)
        
        


if __name__ == "__main__":
    unittest.main()