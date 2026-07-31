#!/usr/bin/python3
"""Unittest for max_integer()."""

import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for max_integer()."""

    def test_ordered_list(self):
        """Test an ordered list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test an unordered list."""
        self.assertEqual(max_integer([3, 1, 7, 5]), 7)

    def test_single_element(self):
        """Test a single-element list."""
        self.assertEqual(max_integer([8]), 8)

    def test_negative_numbers(self):
        """Test a list of negative numbers."""
        self.assertEqual(max_integer([-5, -2, -10]), -2)

    def test_mixed_numbers(self):
        """Test a mixed list."""
        self.assertEqual(max_integer([-1, 0, 3, 2]), 3)

    def test_empty_list(self):
        """Test an empty list."""
        self.assertIsNone(max_integer())

    def test_float_list(self):
        """Test a list of floats."""
        self.assertEqual(max_integer([1.2, 5.6, 2.4]), 5.6)

    def test_duplicate_max(self):
        """Test duplicate maximum values."""
        self.assertEqual(max_integer([5, 5, 2, 5]), 5)


if __name__ == "__main__":
    unittest.main()
