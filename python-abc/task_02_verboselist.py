#!/usr/bin/python3
"""Module that defines a VerboseList class extending the built-in list class."""


class VerboseList(list):
    """class that extends the Python list class."""

    def append(self, item):
        """Override append method to print a message."""
        print(f"Appending [{item}] to the list.")
        super().append(item)

    def extend(self, iterable):
        """Override extend method to print a message."""
        print(f"Extended the list with [{len(iterable)}] items.")
        super().extend(iterable)

    def remove(self, item):
        """Override remove method to print a message."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Override pop method to print a message."""
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
