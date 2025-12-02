#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".foramt(value))
        return True
    except (ValueError, TypeError) as vt:
        print("Exception: {}".format(vt), file=sys.stderr)
        return False
