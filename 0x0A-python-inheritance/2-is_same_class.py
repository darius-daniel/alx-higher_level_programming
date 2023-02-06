#!/usr/bin/python3

"""Contains a function that returns boolean values depending the membership
of an object to a specified class

Prototype: def is_same_class(obj, a_class):

Args:
    obj: must be an object
    a_class: must be a class
"""


def is_same_class(obj, a_class):
    """Contains a function that returns boolean values depending on the
    exact membership of an object to a specified class

    Args:
        obj: an object
        a_class: a class

    Returns:
        True if @obj is an instance of @a_class. False if not.
    """
    if not isinstance(a_class, type):
        raise TypeError("a_class must be a class")
    return type(obj) == a_class
