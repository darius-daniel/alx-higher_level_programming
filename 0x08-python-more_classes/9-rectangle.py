#!/usr/bin/python3

"""Implementation of a class the represents a rectangle
"""


class Rectangle:
    """Defines a Rectangle
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes the new Rectangle instance

        Args:
            self: the current instance of the class
            width: the width of the current instance (defaults to 0)
            height: the height of the current instance (also defaults to zero)
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """Returns the informal string representation of the instance
        """
        if self.height == 0 or self.width == 0:
            return ''

        i = 0
        rectangle = ""
        while (i < self.height):
            rectangle += str(self.print_symbol) * self.width
            if i < self.height - 1:
                rectangle += '\n'
            i += 1

        return rectangle

    def __repr__(self):
        """Returns the formal string representation of the instance, such that
        a new instance can be created from that representation by using eval()
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Prints message to the screen when an instance of Rectangle is
        deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest Rectangle object based on the value of the area

        Args:
            rect_1: first rectangle
            rect_2: second rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width == height == size

        Args:
            cls: the current object class
            size: size of the new instance
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        return cls(size, size)
