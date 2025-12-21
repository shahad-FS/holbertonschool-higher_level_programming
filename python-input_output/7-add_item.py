#!/usr/bin/python3
"""
Adds all CLA to a Python list
and saves to a JSON file
"""
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


file_name = "add_item.json"

try:
    list_arg = load_from_json_file(file_name)
except FileNotFoundError:
    list_arg = []

list_arg.extend(argv[1:])

save_to_json_file(list_arg, file_name)
