#!/usr/bin/python

"""Implementation of a Square object
"""


class Square:
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the class

        Args:
            self: the current Square instance
            size: length of side of the Square instance
            position: tuple of coordinates of the Square instance
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the value of the size attribute of the current Square
        instance.

        Args:
            self: the current Square instance
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of the size attribute of the current Square instance
        to value of value.

        Args:
            self: the current Square instance
            value: the new value of the size attribute
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Retrieves the value of the position attribute of the current Square
        instance

        Args:
            self: the current Square instance
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the value of the position attribute of the current Square
        instance to value of value.

        Args:
            self: the current Square instance
            value: the new value of the position attribute
        """
        if type(value) != tuple or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be tuple of 2 positive integer")
        else:
            self.__position = value

    def area(self):
        """Computes the current square area

        Args:
            self: the current Square instance
        """
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character '#'

        Args:
            self: the current Square instance
        """
        if (self.size == 0):
            print()
        else:
            for h in range(self.size):
                for j in range(self.position[0]):
                    print(" ", end='')
                for k in range(self.size):
                    print("#", end='')
                print()

    def __str__(self):
        """Returns the string representation of the Square object

        Args:
            self: the current instance of this class
        """
        if (self.size == 0):
            print()
        else:
            return_str = ""
            return_str += '\n' * self.position[1]
            for i in range(self.size):
                return_str += " " * self.position[0]
                return_str += "#" * self.size
                if i < self.size - 1:
                    return_str += '\n'
        return return_str
