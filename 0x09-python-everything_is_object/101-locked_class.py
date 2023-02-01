#!/usr/bin/python3

"""A class with no class or instance attributes that prevents the user
from dynamically creating new instance attributes, except if the new instance
atrribute is called first_name
"""


class LockedClass:
    """Defines the locked class
    """
    __slots__ = ["first_name"]

    def __init__(self):
        """Does nothing
        """
        pass
