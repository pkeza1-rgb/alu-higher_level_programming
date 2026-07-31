#!/usr/bin/python3
"""Module that defines append_write."""


def append_write(filename="", text=""):
    """Append a string to the end of a UTF-8 text file.

    Creates the file if it does not exist.
    Returns the number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
