#!/usr/bin/python3
"""Module of function that prints a square with the character # """


def print_square(size):
    """
    prints a square with the character #
    Args:
        size: length of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    square = ""
    for i in range(size):
        square += "#" * size + "\n"
    print(square, end="")
