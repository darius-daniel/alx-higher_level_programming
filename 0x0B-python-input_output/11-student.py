#!/usr/bin/python3

"""Contains a class that defines a student (based on 10-student.py)
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

    def to_json(self, attrs=None):
        """Retrieves the dictionary representation of a Student instance

        Args:
            self: the current instance of the Student class
            attrs: if @attrs is a list of strings, only attribute names in
                   this list must be retrieved. If otherwise, all attributes must
                   be retrieved.
        """
        all_attrs = self.__dict__.copy()

        if type(attrs) is list:
            dict_attr = {}
            for attr in attrs:
                if type(attr) is not str:
                    return all_attrs

            for attr in attrs:
                if attr in self.__dict__:
                    dict_attr[attr] = self.__dict__[attr]

            return dict_attr
        return all_attrs

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance

        Args:
            self: the current Student instance
            json: always a dict
        """
        for key in json:
            if key in self.__dict__:
                self.__dict__[key] = json[key]
