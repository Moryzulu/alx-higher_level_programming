#!/usr.bin.python3
def max_integer(my_list=[]):
    if not my_list:
        return None

    bigger_num = min(my_list)
    for i in my_list:
        if i > bigger_num:
           bigger_num = i

    return bigger_num
