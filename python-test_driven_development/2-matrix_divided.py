#!/usr/bin/python3
""" module of matrix divided function"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix
    Args:
        matrix: list of lists of integers/floats
        div: number of integers/floats to divide the matrix elements by

    Returns:
        A new matrix with all elements divided by div , rounded
        to 2 decimal places
    """

    for array in matrix:
        if not isinstance(array, list):
            raise TypeError("""matrix must be a matrix (list of lists) of 
            integers/floats""")
        if len(array) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for number in array:
            if not isinstance(number, (float, int)):
                raise TypeError("""matrix must be a matrix (list of lists) of 
                        integers/floats""")
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(number / div, 2) for number in array] for array in matrix]
