#!/usr/bin/python3
"""Contains a function that creates an Object from a "JSON file"

Prototype: def load_from_json_file(filename):
    filename: name of the file to read json string from
"""
import json


def load_from_json_file(filename):
    """A function that create an object from a JSON file

    Args:
        filename: a string containing the name of the file the JSON string
                  will be read from
    """
    if filename:
        with open(filename, "r", encoding="utf-8") as file:
            obj = json.load(file)
        return obj
