#!/usr/bin/python3

"""A class based upon the one in 7-base_geometry.py
"""


class BaseGeometry:
    """Adding features to the class defined in 6-base_geometry.py
    """
    def area(self):
        """Raises an Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a value

        Args:
            self: the current instance of the class
            name:  always a string
            value: must be an integer
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Represents a class than inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """Initializes the new instance of the object

        Args:
            width: the width of the rectangle (must be an integer > 0)
            height: the height of the rectangle (must be an integer > 0)
        """
        try:
            self.integer_validator('width', width)
        except TypeError as te:
            raise TypeError(te)
        except ValueError as ve:
            raise ValueError(ve)

        try:
            self.integer_validator('height', height)
        except TypeError as te:
            raise TypeError(te)
        except ValueError as ve:
            raise ValueError(ve)

        self.__width = width
        self.__height = height
