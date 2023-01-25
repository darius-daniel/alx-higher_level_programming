#!/usr/bin/python3

"""This python script build upon previous versions of the same Class
"""


class Square:
    """Defines a square
    """
    def __init__(self, size=0):
        """ Initializes the class

        Args:
          size: size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Computes the current square area

        Args:
            self: the object

        Returns:
            area of the square
        """
        return self.__size ** 2
