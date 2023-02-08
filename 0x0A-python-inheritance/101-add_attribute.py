#!/usr/bin/python3

"""Contains a function that adds a new attribute to an object if the addition
if the addition is possible

Prototype: def add_attribute(obj, name, value):
    obj: object recieving the additional attributes
    name: the name of the attribute
    value: the value of the attribute
"""
def add_attribute(obj, name, value):
    """Adds a new attribute to an object

    Args:
        obj: the object
        name: the attribute name
        value: the attribute value

    Returns:
        nothing. However, if the addition of the new attribute is unsuccessful,
        a TypeError exception is raised
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
