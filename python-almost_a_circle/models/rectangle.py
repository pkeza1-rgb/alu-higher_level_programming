#!/usr/bin/python3
"""This module defines the Rectangle class."""

from models.base import Base


class Rectangle(Base):
    """This class represents a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle instance.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): Horizontal position.
            y (int): Vertical position.
            id (int): Identifier.
        """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Return the rectangle width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the rectangle width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """Return the rectangle height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the rectangle height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """Return the x coordinate."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x coordinate with validation."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """Return the y coordinate."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y coordinate with validation."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """Print the rectangle using the # character."""
        for _ in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        """Return the string representation of the rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id,
            self.__x,
            self.__y,
            self.__width,
            self.__height
        )

    def update(self, *args, **kwargs):
        """Update rectangle attributes using arguments.

        Args:
            args: Non-keyword arguments.
            kwargs: Keyword arguments.
        """
        attributes = ["id", "width", "height", "x", "y"]

        if args:
            for index, value in enumerate(args):
                if index < len(attributes):
                    setattr(self, attributes[index], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation of the rectangle."""
        return {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y
        }
