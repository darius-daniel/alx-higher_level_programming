#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string == "":
        return None

    digit_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    i = 0
    while i < len(roman_string) - 1:
        temp = 0
        while roman_string[i] == roman_string[i + 1]:
            temp += digit_dict[roman_string[i]]
            i += 1

        if digit_dict[roman_string[i]] < digit_dict[roman_string[i - 1]]:
            result += temp
        else:
            result += digit_dict[roman_string[i + 1]] - temp
            i += 1

    return result
