#!/usr/bin/python3

"""A class that inherits from Rectangle in 9-rectangle.py"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square
    """

    def __init__(self, size):
        """Initializes the new instance of the object

        Args:
            size: the length of the sides of the square
                  (must be an integer > 0)
        """
        self.integer_validator('size', size)

        self.__size = size

    def area(self):
        """Returns the area of the rectangle by"""
        return self.__size ** 2

    def __str__(self):
        """Prints the formal string representation of the class"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
