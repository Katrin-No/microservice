import unittest
import api


class TestAPI(unittest.TestCase):

    def test_add(self):
        response = api.API({'a': 3, 'op': '+', 'b': 2})
        self.assertEqual(response.calculate(), 5)

    def test_multiply(self):
        response = api.API({'a': 3, 'op': '*', 'b': 2})
        self.assertEqual(response.calculate(), 6)

    def test_subtract(self):
        response = api.API({'a': 3, 'op': '-', 'b': 2})
        self.assertEqual(response.calculate(), 1)
