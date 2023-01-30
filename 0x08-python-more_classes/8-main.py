#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

my_rect_1 = Rectangle(8, 4)
my_rect_2 = Rectangle(2, 3)

if my_rect_1 is Rectangle.bigger_or_equal(my_rect_1, my_rect_2):
    print("my_rect_1 is bigger or equal to my_rect_2")
else:
    print("my_rect_2 is bigger than my_rect_1")

my_rect_2.width = 10
my_rect_2.height = 5
if my_rect_1 is Rectangle.bigger_or_equal(my_rect_1, my_rect_2):
    print("my_rect_1 is bigger or equal to my_rect_2")
else:
    print("my_rect_2 is bigger than my_rect_1")
