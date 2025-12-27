#!/usr/bin/python3
import sys


total_size = 0
line_count = 0
status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}

def print_stats():
    """Function that prints the statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


try:
    for line in sys.stdin:
        line_count += 1

        data = line.split()
        if len(data) < 2:
            continue

        status_code = data[-2]
        file_size = int(data[-1])

        total_size += file_size


        if status_code in status_codes:
            status_codes[status_code] += 1

        if line_count % 10 == 0:
            print_stats()
except (IndexError, ValueError):
    pass
except KeyboardInterrupt:
    print_stats()
    raise
