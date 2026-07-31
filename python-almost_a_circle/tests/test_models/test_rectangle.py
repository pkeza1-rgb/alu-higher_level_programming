#!/usr/bin/python3
"""Unit tests for Rectangle."""

import unittest
import os
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test Rectangle class."""

    def test_valid_creation(self):
        """Test rectangle creation."""
        r = Rectangle(5, 6)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 6)

    def test_invalid_width_string(self):
        """Test width string validation."""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_invalid_height_string(self):
        """Test height string validation."""
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_invalid_x_string(self):
        """Test x string validation."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_invalid_y_string(self):
        """Test y string validation."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_negative_width(self):
        """Test negative width."""
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_negative_height(self):
        """Test negative height."""
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_display_without_position(self):
        """Test display without x and y."""
        r = Rectangle(2, 3)
        r.display()

    def test_display_x_only(self):
        """Test display with x only."""
        r = Rectangle(10, 12, 1, 0)
        r.display()

    def test_display_y_only(self):
        """Test display with y only."""
        r = Rectangle(10, 12, 0, 1)
        r.display()

    def test_display_with_position(self):
        """Test display with x and y."""
        r = Rectangle(5, 4, 4, 3)
        r.display()

    def test_create_partial(self):
        """Test create with partial dictionary."""
        r = Rectangle.create(id=89)
        self.assertEqual(r.id, 89)

    def test_create_full(self):
        """Test create with all values."""
        r = Rectangle.create(
            id=89,
            width=1,
            height=2,
            x=3,
            y=4
        )
        self.assertEqual(r.x, 3)

    def test_save_none(self):
        """Test saving None."""
        Rectangle.save_to_file(None)
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_save_empty(self):
        """Test saving empty list."""
        Rectangle.save_to_file([])
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_save_objects(self):
        """Test saving rectangles."""
        Rectangle.save_to_file([Rectangle(1, 2)])
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_load_missing(self):
        """Test loading missing file."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_existing(self):
        """Test loading file."""
        Rectangle.save_to_file([Rectangle(1, 2)])
        result = Rectangle.load_from_file()
        self.assertEqual(len(result), 1)


if __name__ == "__main__":
    unittest.main()
