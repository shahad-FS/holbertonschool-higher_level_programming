#!/usr/bin/python3
"""Module for class MyInt that inherits from int"""


class MyInt(int):
    """Class MyInt that inherits form int"""
    def __eq__(self, other):
        """Override the == operator to invert it"""
        return int(self) != int(other)

    def __ne__(self, other):
        """Override the != operator to invert it"""
        return int(self) == int(other)
