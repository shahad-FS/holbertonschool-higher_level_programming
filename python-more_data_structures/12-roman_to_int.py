#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    roman_string = roman_string.upper()
    value = 0
    prev_value = 0
    for char in reversed(roman_string):
        if char in roman_numerals:
            curr_value = roman_numerals[char]
            if curr_value < prev_value:
                value -= curr_value
            else:
                value += curr_value
            prev_value = curr_value
    return value
