#!/usr/bin/python3
"""Unit tests for the Square class."""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for Square."""

    def test_creation(self):
        """Test square creation."""
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_area(self):
        """Test square area."""
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_string(self):
        """Test square string output."""
        s = Square(4, 1, 2, 3)
        self.assertEqual(
            str(s),
            "[Square] (3) 1/2 - 4"
        )

    def test_size_update(self):
        """Test changing square size."""
        s = Square(5)
        s.size = 10
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_dictionary(self):
        """Test dictionary conversion."""
        s = Square(7)
        data = s.to_dictionary()
        self.assertEqual(data["size"], 7)


if __name__ == "__main__":
    unittest.main()
