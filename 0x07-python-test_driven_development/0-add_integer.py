#!/usr/bin/python3

"""Contains a function that computes the sum of two numbers

Prototype: def add_integers(a, b=98):
    a and b must be integers or floats, otherwise raise a TypeError
    exception with the message a must be an integer or b must be an integer
"""


def add_integer(a, b=98):
    """Adds two numbers a and b

    Args:
        a = first integer
        b = second integer (defaults to 98)

    Returns:
        int: the addition of a and b
    """
    if type(a) != float and type(a) != int:
        raise TypeError("a must be an integer")
    elif type(b) != float and type(b) != int:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
