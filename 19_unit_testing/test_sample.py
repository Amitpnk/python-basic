# test_sample.py
# Basic unit testing with Python's built-in unittest module

import unittest

# Function to test
def add(a, b):
    return a + b

def is_even(n):
    return n % 2 == 0

class TestMathFunctions(unittest.TestCase):

    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)

    def test_is_even_true(self):
        self.assertTrue(is_even(4))

    def test_is_even_false(self):
        self.assertFalse(is_even(5))

    def test_add_edge_case(self):
        self.assertEqual(add(0, 0), 0)

if __name__ == "__main__":
    unittest.main()
