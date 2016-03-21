import unittest
from unittest import TestCase
from program import run

class RunTestCase(TestCase):

    def test_returns_hello(self):
        self.assertEqual(run(), "hello")

if __name__ == '__main__':
    unittest.main()
