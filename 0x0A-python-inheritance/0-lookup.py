#!/usr/bin/python3

"""Contains a function that returns the list of available attributes and
methods of an object.

Prototype: def lookup(obj):
    obj: the object
"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object.

    Args:
       obj: the object

    Returns:
        list: a list of all the attributes and methods of the object.
    """
    return (dir(obj))
