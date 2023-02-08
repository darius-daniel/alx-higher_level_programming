#!/usr/bin/python3
import json

"""Contains a function that returns a python data structure from
the JSON string

Prototype: def from_json_string(my_str):
    my_str: a string
"""


def from_json_string(my_str):
    """A function that returns a python data structure from
    the JSON string

    Args:
        my_str: a string

    Raises:
        Exception: if the string cannot be deserialized

    Returns:
        str: the JSON representation of the object
    """
    return json.loads(my_str)
