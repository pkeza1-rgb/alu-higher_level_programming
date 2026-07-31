#!/usr/bin/python3
"""Unit tests for the Base class."""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test the Base class functionality."""

    def test_none_id(self):
        """Test automatic id generation."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_given_id(self):
        """Test custom id assignment."""
        b = Base(42)
        self.assertEqual(b.id, 42)

    def test_id_type(self):
        """Test id values."""
        b = Base(10)
        self.assertEqual(type(b.id), int)

    def test_to_json_string_none(self):
        """Test converting None to JSON."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """Test converting empty list to JSON."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string(self):
        """Test dictionary list conversion."""
        data = [{"id": 1}]
        result = Base.to_json_string(data)
        self.assertEqual(result, '[{"id": 1}]')

    def test_from_json_string_none(self):
        """Test converting None JSON."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """Test empty JSON conversion."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string(self):
        """Test JSON decoding."""
        data = '[{"id": 1}]'
        self.assertEqual(
            Base.from_json_string(data),
            [{"id": 1}]
        )


if __name__ == "__main__":
    unittest.main()
