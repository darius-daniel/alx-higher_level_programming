#!/usr/bin/python3
"""rectangle.py - contains a class that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """A class that inherits from Base and represents a rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new instance of Rectangle

        Args:
            width: (int) the width of the rectangle
            height: (int) the height of the rectangle
            x: (int) the horizontal offset of the rectangle
            y: (int) the vertical offset of the rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Retrieves the value of the protected attribute @self.__width

        Returns: the value of @self.__width
        """
        return self.__width

    @width.setter
    def width(self, new_width):
        """Assigns the value @new_width to the private attribute @self.__width

        Args:
            new_width: (int) the new width of the current Rectangle instance
        """
        if type(new_width) is not int:
            raise TypeError("width must be an integer")
        elif new_width <= 0:
            raise ValueError("width must be > 0")
        self.__width = new_width

    @property
    def height(self):
        """Retrieves the value of the protected attribute @self.__height

        Returns: the value of @self.__height
        """
        return self.__height

    @height.setter
    def height(self, new_height):
        """Assigns the value @new_height to the private attribute
        @self.__height

        Args:
            new_height: (int) the new height of the current Rectangle instance
        """
        if type(new_height) is not int:
            raise TypeError("height must an integer")
        elif new_height <= 0:
            raise ValueError("height must be > 0")
        self.__height = new_height

    @property
    def x(self):
        """Retrieves the value of the protected attribute @self.__x

        Returns: the value of @self.__x
        """
        return self.__x

    @x.setter
    def x(self, new_x):
        """Assigns the value @new_x to the private attribute @self.__x

        Args:
            new_x: (int) the new horizontal offset of the current Rectangle
            instance
        """
        if type(new_x) is not int:
            raise TypeError("x must be an integer")
        elif new_x < 0:
            raise ValueError("x must be >= 0")
        self.__x = new_x

    @property
    def y(self):
        """Retrieves the value of the protected attribute @self.__y

        Returns: the value of @self.__y
        """
        return self.__y

    @y.setter
    def y(self, new_y):
        """Assigns the value @new_y to the private attribute @self.__y

        Args:
            new_y: (int) the new vertical offset of the current Rectangle
            instance
        """
        if type(new_y) is not int:
            raise TypeError("y must be an integer")
        elif new_y < 0:
            raise ValueError("y must be >= 0")
        self.__y = new_y

    def area(self):
        """Computes the value of area value of the Rectangle instance

        Returns:
            int: the area of the Rectangle instance (self.__width * self.__height)
        """
        return self.width * self.height

    def display(self):
        """Prints to stdout the Rectangle instance with the character '#'
        """
        print('\n' * (self.y - 1))
        for i in range(self.height):
            print(" " * self.x, end="")
            print("{}".format('#' * self.width))

    def __str__(self):
        """Print the string representation of the Rectangle instance
        """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
                                                            self.id, self.x,
                                                            self.y, self.width,
                                                            self.height)
