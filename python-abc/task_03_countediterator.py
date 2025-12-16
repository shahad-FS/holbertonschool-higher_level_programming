#!/usr/bin/python3
"""Module that defines a CountedIterator class."""


class CountedIterator:
    """Iterator that counts the number of iterations."""

    def __init__(self, object):
        self.object = iter(object)
        self.counter = 0

    def get_count(self):
        """Return the current value of the counter."""
        return self.counter

    def __next__(self):
        try:
            item = next(self.object)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration
