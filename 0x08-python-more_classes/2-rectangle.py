#!/usr/bin/python3

"""Implementation of a class the represents a rectangle
"""


class Rectangle:
    """Defines a Rectangle
    """
    def __init__(self, width=0, height=0):
        """Initializes the new Rectangle instance

        Args:
            self: the current instance of the class
            width: the width of the current instance (defaults to 0)
            height: the height of the current instance (also defaults to zero)
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Retrieves the value of the width attribute

        Args:
            self: the current instance of the class

        Returns:
            int: the value of self.__width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width attribute to the value of value

        Args:
            self: the current instance of the Rectangle class
            value: the new value of self.__width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieves the value of self.__height

        Args:
            self: the current Rectangle class instance

        Returns:
            int: the value of self.__height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of self.__height to value

        Args:
            self: the current instance of the Rectangle class
            value: the new value of self.__height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Computes the area of the Rectangle instance

        Returns:
            int: the area of the instance (self.__height * self.__width)
        """
        return self.height * self.width

    def perimeter(self):
        """Computes the perimeter of the Rectangle instance

        Args:
            self: the current Rectangle instance

        Returns:
            int: the perimeter of the Rectangle instance
        """
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return (2 * self.height) + (2 * self.width)
