#!/usr/bin/python3
"""Module containing the text_indentation function."""


def text_indentation(text):
    """Print text with two new lines after '.', '?' and ':'.

    Args:
        text: The text to format.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_line = True

    for char in text:
        if new_line and char == " ":
            continue

        new_line = False
        print(char, end="")

        if char in ".?:":
            print("\n")
            new_line = True
