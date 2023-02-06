#!/usr/bin/python3

"""A functions that tests an object for membership in a parent or child class
and returns appopriate boolean values

Prototype: def is_kind_of_class(obj, a_class):

Args:
    obj: must be an object
    a_class: must be a class
"""


def is_kind_of_class(obj, a_class):
    """Tests an object for membership in a parent or child class
    and returns appopriate boolean values.

    Args:
        obj: an instance of the object class
        a_class: a class

    Returns:
        boolean: True if @obj is an instance of @a_class or its ancestors
    """
    if type(a_class) != type:
        raise TypeError("a_class must be a class")
    return isinstance(obj, a_class)
