#!/usr/bin/python3

"""Contains a class that defines a student
"""

class Student:
    """Represents a student
    """
    def __init__(self, first_name, last_name, age):
        """Initializes the class

        Args:
            first_name: the student's first name
            last_name: the student's last name
            age: the student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves the dictionary representation of a Student instance
        """
        return self.__dict__.copy()
