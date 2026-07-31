#!/usr/bin/python3
"""This module defines the Square class."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """This class represents a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square instance.

        Args:
            size (int): Size of the square.
            x (int): Horizontal position.
            y (int): Vertical position.
            id (int): Identifier.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.width
        )

    @property
    def size(self):
        """Return the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the square size."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update square attributes.

        Args:
            args: Non-keyword arguments.
            kwargs: Keyword arguments.
        """
        attributes = ["id", "size", "x", "y"]

        if args:
            for index, value in enumerate(args):
                if index < len(attributes):
                    setattr(self, attributes[index], value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation of the square."""
        return {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y
        }
