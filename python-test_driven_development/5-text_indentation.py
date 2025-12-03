#!/usr/bin/python3
"""Module contains text_indentation function"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :
    Args:
        text: string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    print("\n".join(line.strip() for line in text.split("\n")), end="")
