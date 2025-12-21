#!/usr/bin/python3
"""Module for write_file function."""


def write_file(filename="", text=""):
    """
    Function that writes a string to a text file.
    Return: the number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as file:
        write = file.write(text)

    return write
