#!/usr/bin/python3
import json
"""Module for from_json_string function"""


def from_json_string(my_str):
    """
    Function that return an object(Python data structure)
    represented by a JSON string
    """
    return json.loads(my_str)
