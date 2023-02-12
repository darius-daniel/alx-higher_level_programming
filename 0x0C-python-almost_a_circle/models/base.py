#!/usr/bin/python3
"""Contains a class, Base, which will be the base of all the other classes in
the project. It's goal is to manage id attributes in all subsequent classes
in order to avoid duplicating the same code (and by extension the same bugs)
"""
import json


class Base:
    """The project base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the new instance of this class

        Args:
            self: the current instance of the class
            id: (int) the unique number identifying the current Base instance
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """A converts a list of dictionary string to their JSON representation

        Args:
            list_dictionaries: a list of dictionaries
        """
        json_str = []
        if list_dictionaries is not None:
            for dct in list_dictionaries:
                json_str.append(json.dumps(dct))

        return str(json_str)

    @classmethod
    def save_to_file(cls, list_objs):
        obj_list = []

        if list_objs is not None:
            for obj in list_objs:
                temp_dict = {}
                for key in obj.__dict__.keys():
                    if key != "id":
                        temp_key = key.split("__")[1]
                    else:
                        temp_key = "id"
                    temp_dict[temp_key] = obj.__dict__[key]
                obj_list.append(temp_dict)

            with open("{}.json".format(cls.__name__), "w") as file:
                file.write(Base.to_json_string(obj_list))

