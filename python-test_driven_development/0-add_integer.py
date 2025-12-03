#!/usr/bin/python3
""" Module for function adds two integers"""


def add_integer(a, b=98):
    """
    adds two integer values
    Args:
        a: first integer
        b: second integer

    Returns:
        The Sum of the two integers
    """
    if not isinstance(a, (float, int)):
        if a is not None:
            raise TypeError("a must be an integer")
        raise ValueError("a must be an integer")
    if not isinstance(b, (float, int)):
        if b is not None:
            raise TypeError("b must be an integer")
        raise ValueError("b must be an integer")
    if type(a) is float and type(b) is float:
        return int(a) + int(b)
    elif type(a) is not float and type(b) is float:
        return a + int(b)
    elif type(a) is float and type(b) is not float:
        return int(a) + b
    return a + b
