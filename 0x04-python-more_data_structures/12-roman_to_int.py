#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    if roman_string:
        _dict = [
        ['M', 1000], ['D', 500], ['C', 100], ['L', 50],
        ['X', 10], ['V', 5], ['I', 1]
    ]
    
        num = 0        
        num2 = 0
    for letter in roman_string:
        for elem in _dict:
            if letter == elem[0]:
                if num2 == 0 or num2 >= elem[1]:
                    num += elem[1]
                elif num2 < elem[1]:
                    num += elem[1] - (num2 * 2)

                num2 = elem[1]

    return num
