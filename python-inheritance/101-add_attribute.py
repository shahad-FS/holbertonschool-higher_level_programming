#!/usr/bin/python3
"""Function that adds a new attribute to an object if it's possible"""


def add_attribute(obj, attr_name, attr_value):
    """Function that adds a new attribute to an object if it's possible"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
