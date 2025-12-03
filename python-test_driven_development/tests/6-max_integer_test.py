#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer"""

    def test_ordered_list(self):
        """Test a list in ascending order"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test unordered list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test max at beginning"""
        self.assertEqual(max_integer([9, 2, 3]), 9)

    def test_one_element_list(self):
        """Test list with one element"""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test empty list"""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test list with negative numbers"""
        self.assertEqual(max_integer([-5, -2, -10]), -2)

    def test_mixed_sign_numbers(self):
        """Test list with positive and negative"""
        self.assertEqual(max_integer([-5, 3, -1, 2]), 3)

    def test_all_equal(self):
        """Test all elements equal"""
        self.assertEqual(max_integer([5, 5, 5]), 5)

    def test_floats(self):
        """Test list with floats"""
        self.assertEqual(max_integer([1.5, 2.7, 2.6]), 2.7)

    def test_list_of_strings(self):
        """Test list of strings (max by alphabetical order)"""
        self.assertEqual(max_integer(["a", "z", "m"]), "z")

    def test_string_argument(self):
        """Test passing a string instead of list"""
        self.assertEqual(max_integer("hello"), "o")

    def test_large_list(self):
        """Test large list"""
        self.assertEqual(max_integer(list(range(1000))), 999)


if __name__ == '__main__':
    unittest.main()
