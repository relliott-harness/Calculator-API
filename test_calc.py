import unittest
from app import app

class CalculatorTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_add(self):
        response = self.app.post('/add', json={'x': 10, 'y': 5})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['Message'], 15)

    def test_add_incorrect_params(self):
        response = self.app.post('/add', json={'x': 10})
        self.assertEqual(response.status_code, 301)
        self.assertEqual(response.json['Message'], "ERROR: incorrect number of paramters")

    def test_subtract(self):
        response = self.app.post('/subtract', json={'x': 10, 'y': 5})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['Message'], 5)

    def test_multiply(self):
        response = self.app.post('/multiply', json={'x': 10, 'y': 5})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['Message'], 50)

    def test_divide(self):
        response = self.app.post('/divide', json={'x': 10, 'y': 5})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['Message'], 2.0)

    def test_divide_by_zero(self):
        response = self.app.post('/divide', json={'x': 10, 'y': 0})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.json['Message'], "ERROR: divide by zero")

    def test_divide_incorrect_params(self):
        response = self.app.post('/divide', json={'x': 10})
        self.assertEqual(response.status_code, 301)
        self.assertEqual(response.json['Message'], "ERROR: incorrect number of paramters")

if __name__ == '__main__':
    unittest.main()
