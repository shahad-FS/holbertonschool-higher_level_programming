#!/usr/bin/python3
"""Module contains BaseGeometry class"""


class BaseGeometry:
    """class BaseGeometry"""
    def area(self):
        """public instance method that raises an Exception
        with the message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
