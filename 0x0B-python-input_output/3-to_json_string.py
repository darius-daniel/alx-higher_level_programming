#!/usr/bin/python3
"""Contains a function that returns the JSON representation of an object

Prototype: def to_json_string(my_obj):
    my_obj: a python object
"""
import json


def to_json_string(my_obj):
    """A function that returns the JSON representation of an object

    Args:
        my_obj: a python object

    Raises:
        Exception: if @my_obj can not be serialized

    Returns:
        str: the JSON representation of the object
    """
    return json.dumps(my_obj)
