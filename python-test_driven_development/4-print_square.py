#!/usr/bin/python3
"""Module containing the print_square function."""


def print_square(size):
    """Print a square using the # character.

    Args:
        size: The size of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        if not isinstance(size, float) or size < 0:
            raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float):
        raise TypeError("size must be an integer")

    for i in range(size):
        print("#" * size)
