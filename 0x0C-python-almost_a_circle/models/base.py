#!/usr/bin/python3
"""Contains a class, Base, which will be the base of all the other classes in
the project. It's goal is to manage id attributes in all subsequent classes
in order to avoid duplicating the same code (and by extension the same bugs)
"""


class Base:
    """The project base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the new instance of this class

        Args:
            self: the current instance of the class
            id: (int) the unique number identifying the current Base instance
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
