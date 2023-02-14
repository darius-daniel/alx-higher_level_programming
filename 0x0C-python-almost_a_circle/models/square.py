#!/usr/bin/python3
"""Square class that inherits attributes from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Implementation of a Square object that inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square instance

        Args:
            size: (int) length of each side of the instance
            x: (int) horizontal offset of the square
            y: (int) vertical offset of the square
            id: (int) unique id number of the instance
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Retrieves the value of @self.size
        """
        return self.width

    @size.setter
    def size(self, new_size):
        """Assigns a value to @self.__size

        Args:
            new_size: (int)the value to be assigned
        """
        self.width = new_size
        self.height = new_size

    def update(self, *args, **kwargs):
        """Modifies the attributes of the instance from an argument collector
        or a key-only argument collector

        Args:
            *args: a positional argument collector
            **kwargs: a key-word argument collector
        """
        attrs = ("id", "size", "x", "y")
        if args is not None:
            i = 0
            last_idx = len(attrs) - 1
            for arg in args:
                if i <= last_idx:
                    setattr(self, attrs[i], arg)
                i += 1
        else:
            for key, value in kwargs.items():
                if key in attrs:
                    if key == 'size':
                        setattr(self, "width", value)
                        setattr(self, "height", value)
                    else:
                        setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        sq_dict = {}
        attrs = ("id", "size", "x", "y")
        for attr in attrs:
            for key in self.__dict__.keys():
                toks = key.split("__")
                if attr in toks:
                    sq_dict[attr] = self.__dict__[key]
                elif "height" in toks or "width" in toks:
                    sq_dict["size"] = getattr(self, key)

        return sq_dict

    def __str__(self):
        """[Square] (<id>) <x>/<y> - <size> - in our case, width or height"""
        sq = "[Square] "
        _id = "({:d}) ".format(self.id)
        x_and_y = "{:d}/{:d} - ".format(self.x, self.y)
        size = "{:d}".format(self.size)
        return sq + _id + x_and_y + size
