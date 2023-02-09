#!/usr/bin/python3
"""Unit testing for the width attribute of an instance of the Rectangle class
"""
import unittest
from models.rectangle import Rectangle


class TestAttributes(unittest.TestCase):
    """Performs unit testing for an instance of the Rectangle class
    """
    def test_width(self):
        """Perform tests on the width attribute of the Rectangle instance
        """
        with self.assertRaises(TypeError):
            rect = Rectangle()

        rect = Rectangle(10, 2)

        self.assertEqual(10, rect.width)
        self.assertEqual(2, rect.height)
        self.assertEqual(0, rect.x)
        self.assertEqual(0, rect.y)
        self.assertEqual(2, rect.id)

        with self.assertRaises(TypeError):
            rect.width = None
        with self.assertRaises(TypeError):
            rect.width = '10'
        with self.assertRaises(TypeError):
            rect.width = 10.65
        with self.assertRaises(ValueError):
            rect.width = -10
        with self.assertRaises(ValueError):
            rect.width = 0
        with self.assertRaises(TypeError):
            rect.width = [10]
        with self.assertRaises(TypeError):
            rect.width = (10, )
        with self.assertRaises(TypeError):
            rect.width = {10}
        with self.assertRaises(TypeError):
            rect.width = float('inf')
        with self.assertRaises(TypeError):
            rect.width = float('-inf')
        with self.assertRaises(OverflowError):
            rect.width = int(float('inf'))
        with self.assertRaises(OverflowError):
            rect.width = int(float('-inf'))

    def test_height(self):
        """Performs tests on the height attribute of the Rectangle instance
        """
        with self.assertRaises(TypeError):
            rect = Rectangle()

        rect = Rectangle(10, 2)

        self.assertEqual(10, rect.width)
        self.assertEqual(2, rect.height)
        self.assertEqual(0, rect.x)
        self.assertEqual(0, rect.y)

        rect.height = 5
        self.assertEqual(5, rect.height)

        with self.assertRaises(TypeError):
            rect.height = None
        with self.assertRaises(ValueError):
            rect.height = 0
        with self.assertRaises(ValueError):
            rect.height = -2
        with self.assertRaises(TypeError):
            rect.height = '2'
        with self.assertRaises(TypeError):
            rect.height = [2]
        with self.assertRaises(TypeError):
            rect.height = (2, )
        with self.assertRaises(TypeError):
            rect.height = {2}
        with self.assertRaises(TypeError):
            rect.height = 2.45
        with self.assertRaises(TypeError):
            rect.height = {'height': 2}
        with self.assertRaises(TypeError):
            rect.height = float('inf')
        with self.assertRaises(TypeError):
            rect.height = float('-inf')
        with self.assertRaises(OverflowError):
            rect.height = int(float('inf'))
        with self.assertRaises(OverflowError):
            rect.height = int(float('-inf'))

    def test_x(self):
        """Performs unit tests on the x attribute of the Rectangle instance
        """
        with self.assertRaises(TypeError):
            rect = Rectangle()

        rect = Rectangle(10, 2, 4)

        self.assertEqual(10, rect.width)
        self.assertEqual(2, rect.height)
        self.assertEqual(4, rect.x)
        self.assertEqual(0, rect.y)

        rect.x = 0
        self.assertEqual(0, rect.x)

        with self.assertRaises(TypeError):
            rect.x = None
        with self.assertRaises(ValueError):
            rect.x = -4
        with self.assertRaises(TypeError):
            rect.x = '4'
        with self.assertRaises(TypeError):
            rect.x = 4.0
        with self.assertRaises(TypeError):
            rect.x = [4]
        with self.assertRaises(TypeError):
            rect.x = {4}
        with self.assertRaises(TypeError):
            rect.x = (4, )
        with self.assertRaises(TypeError):
            rect.x = {'x': 4}
        with self.assertRaises(TypeError):
            rect.x = float('inf')
        with self.assertRaises(TypeError):
            rect.x = float('-inf')
        with self.assertRaises(OverflowError):
            rect.x = int(float('inf'))
        with self.assertRaises(OverflowError):
            rect.x = int(float('-inf'))

    def test_y(self):
        """Performs unit tests on the x attribute of the Rectangle instance
        """
        with self.assertRaises(TypeError):
            rect = Rectangle()

        rect = Rectangle(10, 2, 4, 1)

        with self.assertRaises(TypeError):
            rect.y = None
        self.assertEqual(10, rect.width)
        self.assertEqual(2, rect.height)
        self.assertEqual(4, rect.x)
        self.assertEqual(1, rect.y)

        rect.y = 0
        self.assertEqual(0, rect.y)

        with self.assertRaises(ValueError):
            rect.y = -4
        with self.assertRaises(TypeError):
            rect.y = '4'
        with self.assertRaises(TypeError):
            rect.y = 4.0
        with self.assertRaises(TypeError):
            rect.y = [4]
        with self.assertRaises(TypeError):
            rect.y = {4}
        with self.assertRaises(TypeError):
            rect.y = (4, )
        with self.assertRaises(TypeError):
            rect.y = {'x': 4}
        with self.assertRaises(TypeError):
            rect.y = float('inf')
        with self.assertRaises(TypeError):
            rect.y = float('-inf')
        with self.assertRaises(OverflowError):
            rect.y = int(float('inf'))
        with self.assertRaises(OverflowError):
            rect.y = int(float('-inf'))


class TestMethods(unittest.TestCase):
    """Performs tests on all the methods of the Rectangle instance
    """
    def test_area(self):
        """Performs tests on the area method of the Rectangle instance
        """
        with self.assertRaises(TypeError):
            rect = Rectangle()

        rect = Rectangle(6, 3, 2, 1, 21)
        self.assertEqual(6, rect.width)
        self.assertEqual(3, rect.height)
        self.assertEqual(2, rect.x)
        self.assertEqual(1, rect.y)
        self.assertEqual(21, rect.id)
        self.assertEqual(18, rect.area())

        rect.width = 4
        self.assertEqual(12, rect.area())

        rect.height = 4
        self.assertEqual(16, rect.area())

        rect.width = 7
        rect.height = 9
        self.assertEqual(63, rect.area())

        with self.assertRaises(TypeError):
            rect.area(12)
        with self.assertRaises(TypeError):
            rect.area(None)
        with self.assertRaises(TypeError):
            rect.area([])
        with self.assertRaises(TypeError):
            rect.area('12')
        with self.assertRaises(TypeError):
            rect.area((12, ))
        with self.assertRaises(TypeError):
            rect.area({12})
        with self.assertRaises(TypeError):
            rect.area({'key': 12})
        with self.assertRaises(TypeError):
            rect.area(float('inf'))
        with self.assertRaises(TypeError):
            rect.area(float('-inf'))
        with self.assertRaises(OverflowError):
            rect.area(int(float('inf')))
        with self.assertRaises(OverflowError):
            rect.area(int(float('-inf')))
