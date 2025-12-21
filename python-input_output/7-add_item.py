#!/usr/bin/python3
"""Module for add argument to python list script"""
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


file_name = "add_item.json"

try:
    list = load_from_json_file(file_name)
except FileNotFoundError:
    list = []

list.extend(argv[1:])

save_to_json_file(items, file_name)
