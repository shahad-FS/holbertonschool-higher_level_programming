#!/usr/bin/python3
"""Module for load_from_json_file function"""
import json


def load_from_json_file(filename):
    """
    Funcion that creates an object from a "JSON file"
    """
    with open(filename) as file:
        return json.load(file)
