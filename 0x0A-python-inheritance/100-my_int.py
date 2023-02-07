#!/usr/bin/python3

""" Implementation of a class rebellious to its parent """


class MyInt(int):
    """A class the inherits from int but has the == and != operators inverted
    """
    def __eq__(self, other):
        """Invert the equality operator

        Args:
            self: the current instance of the class
            other: the second operand of the == operator
        """
        return int.__ne__(self, other)

    def __ne__(self, other):
        """Inverts the inequality operator

        Args:
            self: the current instance of the class
            other: the second operand of the != operator
        """
        return int.__eq__(self, other)