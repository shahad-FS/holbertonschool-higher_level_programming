#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:

        for array in matrix:
            i = 1
            length = len(array)

            for number in array:
                if i == length:
                    print("{:d}".format(number), end=' ')
                else:
                    print("{:d}".format(number), end =' ')
                i += 1
            print()
