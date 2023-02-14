#!/usr/bin/python3

"""Unit tests for the Square class
"""
import unittest
from models.square import Square
from models.base import Base


class TestSquareAttributes(unittest.TestCase):
    """Performs unit tests on the attributes of a Square instance"""
    def test_square_size(self):
        """Tests on the size attribute of the square"""
        with self.assertRaises(TypeError):
            sq = Square()
        with self.assertRaises(TypeError):
            sq = Square(None)
        with self.assertRaises(ValueError):
            sq = Square(0)
        with self.assertRaises(ValueError):
            sq = Square(-20)
        with self.assertRaises(TypeError):
            sq = Square(4.0)
        with self.assertRaises(TypeError):
            sq = Square('4')
        with self.assertRaises(TypeError):
            sq = Square([6])
        with self.assertRaises(TypeError):
            sq = Square((4, ))
        with self.assertRaises(TypeError):
            sq = Square({4})
        with self.assertRaises(TypeError):
            sq = Square({})
        with self.assertRaises(TypeError):
            sq = Square(float('inf'))
        with self.assertRaises(TypeError):
            sq = Square(float('-inf'))
        with self.assertRaises(OverflowError):
            sq = Square(int(float('inf')))
        with self.assertRaises(OverflowError):
            sq = Square(int(float('-inf')))

        sq = Square(4)
        self.assertEqual(4, sq.size)
        self.assertEqual(4, sq.width)
        self.assertEqual(4, sq.height)
        self.assertEqual(True, sq.width is sq.height)
        self.assertEqual(True, sq.size is sq.width)

        sq_2 = Square(4)
        self.assertEqual(False, sq is sq_2)
        self.assertEqual(False, sq == sq_2)
        self.assertEqual(True, sq.size is sq_2.size)
        self.assertEqual(True, sq.size == sq_2.size)

        with self.assertRaises(TypeError):
            sq.size = None
        with self.assertRaises(TypeError):
            sq.size = '10'
        with self.assertRaises(TypeError):
            sq.size = 10.65
        with self.assertRaises(ValueError):
            sq.size = -10
        with self.assertRaises(ValueError):
            sq.size = 0
        with self.assertRaises(TypeError):
            sq.size = [10]
        with self.assertRaises(TypeError):
            sq.size = (10, )
        with self.assertRaises(TypeError):
            sq.size = {10}
        with self.assertRaises(TypeError):
            sq.size = float('inf')
        with self.assertRaises(TypeError):
            sq.size = float('-inf')
        with self.assertRaises(OverflowError):
            sq.size = int(float('inf'))
        with self.assertRaises(OverflowError):
            sq.size = int(float('-inf'))

    def test_square_x(self):
        """Tests on the x (horizontal offset) attribute of the square
        """
        sq = Square(6)
        self.assertEqual(sq.size, 6)
        self.assertEqual(sq.x, 0)
        self.assertEqual(sq.id, 3)

        sq.x = 4
        self.assertEqual(sq.x, 4)
        sq.x = 220
        self.assertEqual(sq.x, 220)
        sq.x = 1
        self.assertEqual(sq.x, 1)
        sq.x = 10000000000000000000
        self.assertEqual(sq.x, 10000000000000000000)

        with self.assertRaises(TypeError):
            sq.x = None
        with self.assertRaises(TypeError):
            sq.x = 2.5
        with self.assertRaises(ValueError):
            sq.x = -3
        with self.assertRaises(TypeError):
            sq.x = '89'
        with self.assertRaises(TypeError):
            sq.x = [10]
        with self.assertRaises(TypeError):
            sq.x = (9, )
        with self.assertRaises(TypeError):
            sq.x = {1}
        with self.assertRaises(TypeError):
            sq.x = {}
        with self.assertRaises(OverflowError):
            sq.x = int(float("inf"))
        with self.assertRaises(OverflowError):
            sq.x = int(float("-inf"))

    def test_square_y(self):
        """Tests on the y (vertical offset) attribute of the Square instance
        """
        sq = Square(10, 4, 2)
        self.assertTrue(sq.id, 4)
        self.assertTrue(sq.size, 10)
        self.assertTrue(sq.x, 4)
        self.assertTrue(sq.y, 2)

        sq.x = 4
        self.assertEqual(sq.x, 4)
        sq.x = 220
        self.assertEqual(sq.x, 220)
        sq.x = 1
        self.assertEqual(sq.x, 1)
        sq.x = 10000000000000000000
        self.assertEqual(sq.x, 10000000000000000000)

        with self.assertRaises(TypeError):
            sq.y = None
        with self.assertRaises(TypeError):
            sq.y = 2.5
        with self.assertRaises(ValueError):
            sq.y = -3
        with self.assertRaises(TypeError):
            sq.y = '89'
        with self.assertRaises(TypeError):
            sq.y = [10]
        with self.assertRaises(TypeError):
            sq.y = (9, )
        with self.assertRaises(TypeError):
            sq.y = {1}
        with self.assertRaises(TypeError):
            sq.y = {}
        with self.assertRaises(OverflowError):
            sq.y = int(float("inf"))
        with self.assertRaises(OverflowError):
            sq.y = int(float("-inf"))


class TestSquareMethods(unittest.TestCase):
    """Tests on the methods of the class Square
    """
    def test_update(self):
        """Tests on the update method of the class Square
        """
        sq = Square(17)
        self.assertEqual(sq.size, 17)
        self.assertEqual(sq.x, 0)
        self.assertEqual(sq.y, 0)
        # self.assertEqual(sq.id, 8)

        sq.update(0)
        self.assertEqual(sq.size, 17)
        self.assertEqual(sq.x, 0)
        self.assertEqual(sq.y, 0)
        self.assertEqual(sq.id, 0)

        sq.update(22, 3)
        self.assertEqual(sq.size, 3)
        self.assertEqual(sq.x, 0)
        self.assertEqual(sq.y, 0)
        self.assertEqual(sq.id, 22)

        sq.update(37, 5, 4)
        self.assertEqual(sq.size, 5)
        self.assertEqual(sq.x, 4)
        self.assertEqual(sq.y, 0)
        self.assertEqual(sq.id, 37)

        sq.update(11, 24, 3, 2)
        self.assertEqual(sq.size, 24)
        self.assertEqual(sq.x, 3)
        self.assertEqual(sq.y, 2)
        self.assertEqual(sq.id, 11)

        sq.update(11, 15, 1, 4, 28)
        self.assertEqual(sq.size, 15)
        self.assertEqual(sq.x, 1)
        self.assertEqual(sq.y, 4)
        self.assertEqual(sq.id, 11)

        sq.update(x=3, size=12, id=89, y=4, q="never mind")
        self.assertEqual(sq.size, 12)
        self.assertEqual(sq.x, 3)
        self.assertEqual(sq.y, 4)
        self.assertEqual(sq.id, 89)
        with self.assertRaises(AttributeError):
            print(sq.q)

        # ===========================================================
        # Testing behaviour in names of keyword-only arguments incorrectly
        # typed
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        # If 'y' is incorrectly spelled
        sq.update(Y=9, id=98, size=18, x=4)
        self.assertEqual(sq.id, 98)
        self.assertEqual(sq.y, 4)
        self.assertEqual(sq.x, 4)
        self.assertEqual(sq.size, 18)
        with self.assertRaises(AttributeError):
            print(sq.Y)

        # if 'id' was incorrectly spelled
        sq.update(y=2, di=55, size=3, x=20)
        self.assertEqual(sq.id, 98)
        self.assertEqual(sq.y, 2)
        self.assertEqual(sq.x, 20)
        self.assertEqual(sq.size, 3)
        with self.assertRaises(AttributeError):
            print(sq.di)

        # if size is spelled incorrectly
        sq.update(x=1, y=0, sieze=9, id=90)
        self.assertEqual(sq.x, 1)
        self.assertEqual(sq.y, 0)
        self.assertEqual(sq.size, 3)
        self.assertEqual(sq.id, 90)
        with self.assertRaises(AttributeError):
            print(sq.sieze)

        # if x is spelled incorrectly
        sq.update(x_=12, y=6, size=11, id=72)
        self.assertEqual(sq.x, 1)
        self.assertEqual(sq.y, 6)
        self.assertEqual(sq.size, 11)
        self.assertEqual(sq.id, 72)
        with self.assertRaises(AttributeError):
            print(sq.x_)

    def test_to_dictionary(self):
        """Tests on the 'to_dictionary' method of the Square class
        """
        sq = Square(5)
        sq_dict = {'size': 5, 'x': 0, 'y': 0, 'id': 5}
        self.assertDictEqual(sq_dict, sq.to_dictionary())

        sq = Square(8, 2)
        sq_dict = {'id': 6, 'size': 8, 'x': 2, 'y': 0}
        self.assertDictEqual(sq_dict, sq.to_dictionary())

        sq = Square(15, 1, 3)
        sq_dict = {'id': 7, 'size': 15, 'x': 1, 'y': 3}
        self.assertDictEqual(sq_dict, sq.to_dictionary())

        sq = Square(45, 13, 5, 89)
        sq_dict = {'id': 89, 'size': 45, 'x': 13, 'y': 5}
        self.assertDictEqual(sq_dict, sq.to_dictionary())

        with self.assertRaises(TypeError):
            sq = Square(3, 6, 2, 101, 2891)
