#!/usr/bin/python3

"""Contains a class that inherits from list and does some thigns differently
"""


class MyList(list):
    """A class that inherits from list
    """
    def print_sorted(self):
        """Prints the list, but with the elements sorted in ascending
        order

        Args:
            self: the current instance of the class
        """
        sorted_list = self.copy()
        sorted_list.sort()
        print(sorted_list)
