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
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end='')
                print()
