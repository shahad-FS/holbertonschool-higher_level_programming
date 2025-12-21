#!/usr/bin/python3
"""Module for add_items script"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


file_name = "add_item.json"

try:
    load_from_json_file(file_name)
except Exception:
    items = []

for arg in sys.argv[1:]:
    items.append(arg)

save_to_json_file(items, file_name)
