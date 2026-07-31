#!/usr/bin/python3
"""Unit tests for the Base class."""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for Base."""

    def test_id_increment(self):
        """Test automatic id generation."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_custom_id(self):
        """Test assigning a custom id."""
        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_to_json_string(self):
        """Test converting dictionaries to JSON."""
        data = [{"id": 1}]
        result = Base.to_json_string(data)
        self.assertIsInstance(result, str)

    def test_empty_json_string(self):
        """Test empty JSON conversion."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_from_json_string(self):
        """Test converting JSON back to list."""
        data = '[{"id": 1}]'
        result = Base.from_json_string(data)
        self.assertEqual(result, [{"id": 1}])


if __name__ == "__main__":
    unittest.main()
