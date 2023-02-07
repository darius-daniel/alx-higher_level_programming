#!/usr/bin/python3

"""A class that inherits from BaseGeometry in 7-base_geometry.py"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a class than inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """Initializes the new instance of the object

        Args:
            width: the width of the rectangle (must be an integer > 0)
            height: the height of the rectangle (must be an integer > 0)
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)

        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the rectangle by"""
        return self.__width * self__height

    def __str__(self):
        """Prints the formal string representation of the class"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
