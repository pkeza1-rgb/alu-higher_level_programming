#!/usr/bin/python3
"""Unit tests for the Rectangle class."""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle."""

    def test_creation(self):
        """Test rectangle creation."""
        r = Rectangle(5, 10)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)

    def test_area(self):
        """Test rectangle area."""
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_string(self):
        """Test rectangle string output."""
        r = Rectangle(2, 3, 1, 1, 5)
        self.assertEqual(
            str(r),
            "[Rectangle] (5) 1/1 - 2/3"
        )

    def test_invalid_width(self):
        """Test invalid width."""
        with self.assertRaises(TypeError):
            Rectangle("5", 3)

    def test_negative_height(self):
        """Test invalid height."""
        with self.assertRaises(ValueError):
            Rectangle(3, -1)

    def test_dictionary(self):
        """Test dictionary conversion."""
        r = Rectangle(3, 4)
        self.assertEqual(
            r.to_dictionary()["width"],
            3
        )


if __name__ == "__main__":
    unittest.main()
