#!/usr/bin/python3
"""Contains a function that writes an Object to a text file using a JSON
representation

Prototype: def save_to_json_file(my_obj, filename):
    my_obj: a python Object
    filename: a string containing the name and/or path to be written to.
"""
from json import dump


def save_to_json_file(my_obj, filename):
    """A function that writes an Object to a text file using a JSON
    representation

    Args:
        my_obj: a python object
        filename: a string containing the name and/or path of the file to be
                  written to
    """
    if filename:
        with open(filename, 'w', encoding="utf-8") as file:
            dump(my_obj, file)
