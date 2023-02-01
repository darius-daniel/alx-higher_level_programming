#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Performs unit testing for the code in 6-max_integer.py
    """
    def test_max_integer(self):
        l = [1, 21, 12, 42, 100, 10000]
        self.assertEqual(max_integer(l), 10000)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([20]), 20)
        self.assertEqual(max_integer([1, 5, 4, 0]), 5)
        self.assertEqual(max_integer([-3, -19, -10]), -3)
        self.assertRaises(TypeError, max_integer("1, 21, 12, 35, 100"))
        self.assertRaises(TypeError, max_integer((1, 21, 12, 42, 100, 1000)))
