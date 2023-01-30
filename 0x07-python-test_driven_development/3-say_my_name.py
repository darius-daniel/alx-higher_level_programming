#!/usr/bin/python3

"""Contains a function that prints "My name is <first name> <last name>"

Prototype: def say_my_name(first_name, last_name=""):
    first_name: must be a string, otherwise raise a TypeError exception
                with the message, "first_name must be a string"
    last_name: must be a string, otherwise raise a TypeError exception
               with the message, "last_name must be a string"
"""


def say_my_name(first_name, last_name=""):
    """Prints "My name is <first name> <last name>"

    Args:
        first_name: person's first name (must be a string)
        last_name: person's surname name (defaults to an empty string and must be string)
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    elif type(last_name) != str:
        raise TypeError("last_name must be a string")
    else:
        return "My name is {} {}".format(first_name, last_name)
