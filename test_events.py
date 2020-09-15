import unittest
from app import app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        
    def test_index_page_works(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 301)

if __name__ == '__main__':
    unittest.main()

