#!/usr/bin/python3
"""Unit tests for Rectangle."""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test Rectangle class."""

    def test_creation(self):
        """Test rectangle creation."""
        r = Rectangle(5, 6)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 6)

    def test_id(self):
        """Test rectangle id."""
        r = Rectangle(2, 3, 0, 0, 99)
        self.assertEqual(r.id, 99)

    def test_area(self):
        """Test rectangle area."""
        r = Rectangle(4, 5)
        self.assertEqual(r.area(), 20)

    def test_width_type(self):
        """Test width validation."""
        with self.assertRaises(TypeError):
            Rectangle("4", 5)

    def test_height_type(self):
        """Test height validation."""
        with self.assertRaises(TypeError):
            Rectangle(4, "5")

    def test_width_value(self):
        """Test width positive validation."""
        with self.assertRaises(ValueError):
            Rectangle(0, 5)

    def test_height_value(self):
        """Test height positive validation."""
        with self.assertRaises(ValueError):
            Rectangle(5, 0)

    def test_x_negative(self):
        """Test x validation."""
        with self.assertRaises(ValueError):
            Rectangle(5, 5, -1)

    def test_y_negative(self):
        """Test y validation."""
        with self.assertRaises(ValueError):
            Rectangle(5, 5, 0, -1)

    def test_string(self):
        """Test rectangle string."""
        r = Rectangle(4, 6, 2, 1, 10)
        self.assertEqual(
            str(r),
            "[Rectangle] (10) 2/1 - 4/6"
        )

    def test_dictionary(self):
        """Test rectangle dictionary."""
        r = Rectangle(3, 4)
        self.assertEqual(
            r.to_dictionary(),
            {
                "id": r.id,
                "width": 3,
                "height": 4,
                "x": 0,
                "y": 0
            }
        )

    def test_update_args(self):
        """Test positional update."""
        r = Rectangle(1, 1)
        r.update(5, 6, 7, 8, 9)
        self.assertEqual(r.id, 5)
        self.assertEqual(r.width, 6)
        self.assertEqual(r.height, 7)
        self.assertEqual(r.x, 8)
        self.assertEqual(r.y, 9)

    def test_update_kwargs(self):
        """Test keyword update."""
        r = Rectangle(1, 1)
        r.update(width=8, height=9)
        self.assertEqual(r.width, 8)
        self.assertEqual(r.height, 9)


if __name__ == "__main__":
    unittest.main()
