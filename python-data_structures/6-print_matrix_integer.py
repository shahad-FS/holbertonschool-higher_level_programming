#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
    else:
        for array in matrix:
            for index, number in enumerate(array):
                if index < len(array) - 1:
                    print("{:d}".format(number), end=' ')
                else:
                    print("{:d}".format(number))
