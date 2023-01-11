#!/usr/bin/python3

def uniq_add(my_list=[]):
    if my_list:
        sum = 0
        for num in my_list:
            if my_list.count(num) == 1:
                sum += num
        return sum
