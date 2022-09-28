#!/usr/bin/python3
import sys

if __name__ == '__main__':
    argd = sys.argv
    length = len(argd) - 1

    if length > 1:
        print(length, 'arguments:')
        for i in range(1, length + 1):
            print('{:d}: {}'.format(i, argd[i]))
    elif length == 1:
        print(length, 'argument:')
        for i in range(1, length + 1):
            print('{:d}: {}'.format(i, argd[i]))
    elif length == 0:
        print(length, 'arguments.')
