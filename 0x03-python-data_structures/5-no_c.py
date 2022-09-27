#!/usr/bin/python3
def no_c(my_string):
    str_noc = ''
    for i in my_string:
        if i != 'C' and i != 'c':
            str_noc += i

    return str_noc
