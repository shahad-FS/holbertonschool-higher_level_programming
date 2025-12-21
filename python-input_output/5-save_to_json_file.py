#!/usr/bin/python3
"""Module for save_to_json_file function"""
import json


def save_to_json_file(my_obj, filename):
    """
    Function that writes an object to a text file
    using a JSON representation
    """
    with open(filename, "w") as file:
        return jsoun.dump(my_obj, file)
