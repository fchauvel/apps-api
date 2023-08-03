from unittest import TestCase
from appsapi.runner import app
from fastapi.testclient import TestClient


class SampleTests(TestCase):

    def setUp(self):
        self.client = TestClient(app)

    def test_works(self):
        response = self.client.get("/test")
        self.assertEqual(200, response.status_code)
        self.assertEqual({"message": "Hello World"},
                           response.json())
