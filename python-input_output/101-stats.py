#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics:
- Total file size
- Number of lines by HTTP status code
Prints statistics every 10 lines and on keyboard interruption.
"""


def print_stats():
    """Function that prints the statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


if __name__ == "__main__":
    import sys

    total_size = 0
    line_count = 0
    status_codes = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }

    try:
        for line in sys.stdin:
            data = line.split()
            if len(data) < 2:
                continue

            try:
                status_code = int(data[-2])
                file_size = int(data[-1])
            except ValueError:
                continue

            total_size += file_size
            line_count += 1

            if status_code in status_codes:
                status_codes[status_code] += 1

            if line_count % 10 == 0:
                print_stats()

    except KeyboardInterrupt:
        print_stats()
        raise

    if line_count % 10 != 0 or line_count == 0:
        print_stats()
