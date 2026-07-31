#!/usr/bin/python3
"""Unit tests for Square."""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test Square class."""

    def test_creation(self):
        """Test square creation."""
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_area(self):
        """Test square area."""
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_string(self):
        """Test square string."""
        s = Square(4, 1, 2, 3)
        self.assertEqual(
            str(s),
            "[Square] (3) 1/2 - 4"
        )

    def test_size_setter(self):
        """Test square size update."""
        s = Square(5)
        s.size = 10
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_update_args(self):
        """Test positional update."""
        s = Square(5)
        s.update(10, 7, 2, 3)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_update_kwargs(self):
        """Test keyword update."""
        s = Square(5)
        s.update(size=8, x=4)
        self.assertEqual(s.size, 8)
        self.assertEqual(s.x, 4)

    def test_dictionary(self):
        """Test square dictionary."""
        s = Square(5)
        self.assertEqual(
            s.to_dictionary()["size"],
            5
        )


if __name__ == "__main__":
    unittest.main()
