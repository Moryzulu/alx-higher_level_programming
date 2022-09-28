#!/usr/bin/python3
def roman_to_int(roman_string):
    num = 0
    if roman_string:
        _dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000}
        for a in roman_string:
            num += _dict.get(a, 0)
    return num
