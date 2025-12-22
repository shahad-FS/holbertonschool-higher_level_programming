#!/usr/bin/python
"""Module for serializing and deserializing"""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize data to JSON and save to a file"""
    with open(filename, "w") as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """Load data from a file and deserialize from JSON"""
    with open(filename, "r") as file:
        return json.load(file)
