import unittest
from app import app
import json


class TestCreateResponse(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_create_response(self):
        response = self.app.get(
            '/create-response/What-services-does-company-provide?')
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.data)


class TestCreateResponse(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_create_response(self):
        response = self.app.get(
            '/create-response/how-can-I-contact-the-company?')
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.data)

        print(response.data)

    def test_create_response_invalid_prompt(self):
        response = self.app.get('/create-response/')
        self.assertEqual(response.status_code, 404)

    def test_create_response_invalid_prompt(self):
        response = self.app.get('/create-response/')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
