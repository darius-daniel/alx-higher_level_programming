#!/usr/bin/python3
import json

"""Contatins a function that returns the JSON representation of an object

Prototype: def to_json_string(my_obj):
    my_obj: a python object
"""


def to_json_string(my_obj):
    """A function that returns the JSON representation of an object

    Args:
        my_obj: a python object

    Returns:
        string: the JSON representation of the object
    """
    return json.dumps(my_obj)
