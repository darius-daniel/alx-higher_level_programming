#!/usr/bin/python3

inherits_from = __import__('4-inherits_from').inherits_from

a = 'a'
if inherits_from(a, int):
    print("{} inherited from the class {}".format(a, int.__name__))
if inherits_from(a, float):
    print("{} inherited from the class {}".format(a, float.__name__))
if inherits_from(a, object):
    print("{} inherited from the class {}".format(a, object.__name__))
