#!/usr/bin/python3
"""This module defines the Base class used for managing object identifiers."""

import json


class Base:
    """This class manages the id attribute for all project classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance.

        Args:
            id (int): Optional identifier for the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dictionaries.

        Args:
            list_dictionaries (list): List of dictionaries.

        Returns:
            str: JSON representation.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON representation of objects to a file.

        Args:
            list_objs (list): List of Base instances.
        """
        filename = cls.__name__ + ".json"

        if list_objs is None:
            list_objs = []

        dictionaries = [obj.to_dictionary() for obj in list_objs]

        with open(filename, "w") as file:
            file.write(cls.to_json_string(dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """Return a list from a JSON string.

        Args:
            json_string (str): JSON formatted string.

        Returns:
            list: Python list representation.
        """
        if json_string is None or json_string == "":
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with attributes initialized from a dictionary.

        Args:
            dictionary (dict): Attributes to assign.

        Returns:
            object: A new instance of the class.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()

        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """Load instances from a JSON file.

        Returns:
            list: List of created instances.
        """
        filename = cls.__name__ + ".json"

        try:
            with open(filename, "r") as file:
                json_string = file.read()
        except FileNotFoundError:
            return []

        dictionaries = cls.from_json_string(json_string)

        return [cls.create(**item) for item in dictionaries]
