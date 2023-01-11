#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        biggest = 0
        name = ""
        for student in a_dictionary.keys():
            if a_dictionary[student] > biggest:
                biggest = a_dictionary[student]
                name = student
        return name
    else:
        return None
