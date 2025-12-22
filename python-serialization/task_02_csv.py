#!/usr/bin/python
"""Module for converting CSV to JSON"""
import csv
import json


def csv_to_json(csv_filename):
    """Convert CSV file to JSON format"""
    try:
        with open(csv_filename, "r") as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)
        json_filename = "data.json"
        with open(json_filename, "w") as json_file:
            json.dump(data, json_file, indent=4)
            return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
