#!/usr/bin/python3

"""A function that returns check if the object is an instance of a class
that inherited (directly or indirectly) from the specified class: otherwise
False

Prototype: def inherits_from(obj, a_class):

    obj: must be an instance of the object class
    a_class: must be a class
"""


def inherits_from(obj, a_class):
    """A function that returns check if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class: otherwise
    False

    Args:
        obj: the object
        a_class: a class

    Returns:
        bool: True if @obj is an instance of a class that inherited (directly
        or indirectly) from the specified class; otherwise False
    """
    if type(a_class) != type:
        raise TypeError("a_class must be a class")
    return issubclass(type(obj), a_class)
