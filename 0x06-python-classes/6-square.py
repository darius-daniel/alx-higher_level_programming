#!/usr/bin/python3

"""This python script build upon previous versions of the same Class
"""


class Square:
    """Defines a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """ Initializes the class

        Args:
          size: size of the square
          position: a tuple of two integers that represent the coordinates
                    of the square
        """
        self.size = size
        self.position = position

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
            for h in range(self.size):
                for j in range(self.position[0]):
                    print(" ", end='')
                for k in range(self.size):
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
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
