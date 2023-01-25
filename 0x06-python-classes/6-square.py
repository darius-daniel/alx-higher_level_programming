#!/usr/bin/python3

"""This python script build upon previous versions of the same Class
"""


class Square:
    """Defines a square
    """
    def __init__(self, size=0, position=0):
        """ Initializes the class

        Args:
          size: size of the square
          position: a tuple of two integers that represent the coordinates
                    of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if type(position) != tuple or len(position) != 2\
                or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        """Computes the current square area

        Args:
            self: the object

        Returns:
            area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """Retrieves the value of the square instance

        Args:
            self: instance of the class

        Returns:
            the area of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Retrieves the value of the size of the square instance

        Args:
            self: the instance of the class
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """Prints in stdout the square with the character '#'
        """
        if (self.size == 0):
            print()
        else:
            for i in range(self.__position[1]):
                for j in range(self.__position[0]):
                    print(" ", end='')
                for k in range(self.__size):
                    print("#", end='')
                print()

    @property
    def position(self):
        """Retrieves the value of the position attribute
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the value of position to value
        """
        if type(value) != tuple or len(value) != 2\
                or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
