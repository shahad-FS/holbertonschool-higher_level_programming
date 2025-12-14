#!/usr/bin/python3
"""Module for print_sorted function"""


class MyList(list):
    """class MyList that inherits from list"""
    def print_sorted(self):
        """public instance method that prints the list,
        but sorted (ascending sort)"""
        print(sorted(self))
