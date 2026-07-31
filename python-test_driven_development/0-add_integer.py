#!/usr/bin/python3
"""Module containing the add_integer function."""


def add_integer(a, b=98):
    """Return the addition of two integers.

    Args:
        a: The first integer or float.
        b: The second integer or float.

    Raises:
        TypeError: If a or b is not an integer or float.

    Returns:
        The sum of a and b as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
