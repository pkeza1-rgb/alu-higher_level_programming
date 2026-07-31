#!/usr/bin/python3
"""Module that defines load_from_json_file."""

import json


def load_from_json_file(filename):
    """Create an object from a JSON file."""
    with open(filename, encoding="utf-8") as file:
        return json.load(file)
