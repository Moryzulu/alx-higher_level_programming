#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for number_z in matrix:
            i = 1
            length = len(number_z)

            for num in number_z:
                if i == length:
                    print('{:d}'.format(num), end='')
                else:
                    print('{:d}'.format(num), end=' ')
                i += 1

            print()
