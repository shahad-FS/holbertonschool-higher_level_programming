#!/usr/bin/python
"""Module for converting CSV to JSON"""
import csv
import json


def csv_to_json(csv_filename):
    """Convert CSV file to JSON file"""
    try:
         with open(csv_filename, mode='r', newline='', encoding='utf-8') as csv_file:
              csv_reader = csv.DictReader(csv_file)
              data = [row for row in csv_reader]
         
         with open('data.json', mode='w', encoding='utf-8') as json_file:
              json.dump(data, json_file, indent=4)
         
         return True
    except FileNotFoundError:
         return False
