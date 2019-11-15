from django.test import TestCase
from .basicTest import add, subtract


class BasicTestTests(TestCase):
    # Any initialization I want
    def setUp(self):
        pass

    # def ANYTHING_test -> will not work, the functions have to start with test
    def test_add_numbers(self):
        """Test that 2 numbers are added together correctly"""
        a, b = 5, 6
        expected = a + b
        # check for equality, real vs expected
        self.assertEqual(add(a, b), expected)

    def test_sub_numbers(self):
        """Test that 2 values are substracted and returned correctly"""
        a, b = 5, 10
        expected = b - a
        self.assertEqual(subtract(b, a), expected)
