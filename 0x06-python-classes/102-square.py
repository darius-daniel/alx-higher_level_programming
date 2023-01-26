#!/usr/bin/python3

"""Implementation of a square that is based on ./4-square.py
"""


class Square:
    """Represents a square
    """
    def __init__(self, size=0):
        """Initializes the square with instance attributes

        Args:
            self: the current Square instance
            size: size of the current Square instance. Defaults to 0
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the value of the size attribute

        Args:
            self: the current Square instance
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the value of self.__size to the value of value
        Performs a pair of checks first.

        Args:
            self: the current Square instance
            value: must be an int or a float
        """
        if type(value) != float and type(value) != int:
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Computes the current square area

        Args:
            self: the current Square instance
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Compares two Square instances for equality based on the values of
        their size attributes.

        Args:
            self: the first Square instance
            other: the second Square instance
        """
        if self.size == other.size:
            return True
        else:
            return False

    def __ne__(self, other):
        """Compares two Square instances for equality based on the values of
        their size attributes. It is the opposite of the __eq__ method

        Args:
            self: the first Square instance
            other: the second Square instance
        """
        if self.size == other.size:
            return False
        else:
            return True

    def __gt__(self, other):
        """Computes if one Square instance is greater than another based on the
        values of their size attributes

        Args:
            self: the first Square instance
            other: the second Square instance
        """
        if self.size > other.size:
            return True
        else:
            return False

    def __ge__(self, other):
        """Computes if one Square instance is greater than or equal to another
        based on the values of their size attributes

        Args:
            self: the first Square instance
            other: the second Square instance
        """
        if self.size >= other.size:
            return True
        else:
            return False

    def __lt__(self, other):
        """Computes if one Square instance is less than another based on the
        values of their size attributes

        Args:
            self: the first Square instance
            other: the second Square instance
        """
        if self.size < other.size:
            return True
        else:
            return False

    def __le__(self, other):
        """Computes if one Square instance is less than or equal to another
        based on the values of their size attributes.

        Args:
            self: the first Square instance
            other: the second Square instance
        """
        if self.size <= other.size:
            return True
        else:
            return False
