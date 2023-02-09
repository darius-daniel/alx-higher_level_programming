#!/usr/bin/python3
"""Contains a function that returns the dictionary description with simple
with simple data structure (list, dict, str, int, bool) for JSON serialization

Prototype: def class_to_json(obj):
    obj: instance of a class
"""


def class_to_json(obj):
    """A function that returns the dictionary description with simple data
    structure for JSON serialization

    Args:
        obj: an instance of a class
    """
    dict_rep = {}
    if '__dict__' in dir(obj):
        dict_rep = obj.__dict__.copy()

    return dict_rep
