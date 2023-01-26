#!/usr/bin/python3

"""Implementation of a singly linked list
"""


class Node:
    """Represents a Node
    """
    def __init__(self, data, next_node=None):
        """Initializes the class with the provided attributes
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves the value of the data attribute
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the value of __data to value
        """
        if type(value) != int and value is not None:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the address of the next node in the linked list
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and type(value) != Node:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list
    """
    def __init__(self):
        """Initializes the class
        """
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new node into the correct sorted position in the list
        (increasing order)

        Args:
            value: the number to be contained in the newly inserted node
        """
        current = self.__head

        while current is not None and value > current.data:
            previous = current
            current = current.next_node

        new = Node(value, current)
        if (current == self.__head):
            self.__head = new
        else:
            previous.next_node = new

    def __str__(self):
        """Prints the string representation of the linked list to stdout
        """
        current = self.__head
        return_value = ""

        while current is not None:
            return_value += str(current.data)
            return_value += '\n'
            current = current.next_node

        return return_value
