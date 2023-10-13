import unittest
from fastapi.testclient import TestClient
from main import app  

class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_get_producer_max_interval(self):
        response = self.client.get("/producer_max_interval")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("max", data)

    def test_get_producer_min_interval(self):
        response = self.client.get("/producer_min_interval")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("min", data)

    def test_get_awards_interval(self):
        response = self.client.get("/awards_interval")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("min", data)
        self.assertIn("max", data)

if __name__ == "__main__":
    unittest.main()
