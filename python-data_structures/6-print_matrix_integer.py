#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for array in matrix:
        for number in array:
            print("{:d}".format(number), end=' ')
        print()
