#!/usr/bin/python3
"""Contains a class, Base, which will be the base of all the other classes in
the project. It's goal is to manage id attributes in all subsequent classes
in order to avoid duplicating the same code (and by extension the same bugs)
"""
import json
import os
import csv


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
                json_str.append(dct)

        return json.dumps(json_str)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file

        Args:
            cls: a user-defined class
            list_objs: a list of instances that inherit from Base
        """
        obj_list = []

        if list_objs is not None:
            for obj in list_objs:
                temp_dict = {}
                for key in obj.__dict__.keys():
                    temp_key = key
                    if key != "id":
                        temp_key = key.split("__")[1]
                        if temp_key == 'width' or temp_key == 'height':
                            temp_key = 'size'
                    temp_dict[temp_key] = obj.__dict__[key]

                obj_list.append(temp_dict)

        with open("{}.json".format(cls.__name__), "w") as file:
            file.write(cls.to_json_string(obj_list))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation of json_string

        Args:
            json_string: (list)

        Returns:

        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates new instance of a class that inherits from Base with all
        all attributes already set

        Args:
            cls: the class of the new instance
            **dictionary: a keyword-only argument collector for dictionaries

        Returns:
            the new instance of @cls with all attributes set
        """
        if cls.__name__ == "Rectangle":
            temp = cls(99, 99)
        else:
            temp = cls(99)
        temp.update(**dictionary)

        return temp

    @classmethod
    def load_from_file(cls):
        """Creates instances of a class @cls from string in a JSON file.

        Args:
            cls: the class using the method

        Returns:
            if file doesn't exist: an empty list
            if file exists: a list of instances
        """
        cls_instances = []
        file_name = "{}.json".format(cls.__name__)

        if os.path.exists(file_name) is False:
            return []

        with open("{}.json".format(cls.__name__), "r") as file:
            json_string = file.read()

        cls_dict_list = Base.from_json_string(json_string)
        for dct in cls_dict_list:
            cls_instances.append(cls.create(**dct))

        return cls_instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes in CSV

        Args:
            cls: the class calling the method
            list_objs: a list of objs to be serialized
        """
        filename = "{}.csv".format(cls.__name__)
        if cls.__name__ == "Rectangle":
            form = ('id', 'width', 'height', 'x', 'y')
        else:
            form = ('id', 'size', 'x', 'y')

        values = []
        if list_objs:
            for obj in list_objs:
                obj_attr_values = []
                for item in form:
                    obj_attr_values.append(getattr(obj, item))
                values.append(obj_attr_values)

        with open(filename, "w") as file:
            writer = csv.writer(file, delimiter=',')
            if values:
                for attr_list in values:
                    writer.writerow(attr_list)

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes from CSV

        Args:
            cls: the class calling the method
            list_objs: a list of objs to be serialized
        """
        filename = "{}.csv".format(cls.__name__)
        if not os.path.exists(filename):
            return []

        if cls.__name__ == "Rectangle":
            form = ('id', 'width', 'height', 'x', 'y')
        else:
            form = ('id', 'size', 'x', 'y')

        with open(filename, "r") as file:
            reader = csv.reader(file, delimiter=',')
            obj_list = []
            for row in reader:
                obj_dict = {}
                for i in range(len(form)):
                    key, value = form[i], int(row[i])
                    obj_dict[key] = value
                new_cls_obj = cls.create(**obj_dict)
                obj_list.append(cls.create(new_cls_obj))

        return obj_list
