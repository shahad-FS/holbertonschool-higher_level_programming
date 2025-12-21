#!/usr/bin/python3
"""Module for Student class"""


class Student:
    """Class Student"""
    def __init__(self, first_name, last_name, age):
        """Initialize a new Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary representation of a Student."""
        if attrs is None:
            return self.__dict__
        else:
            return{key: value for key, value in self.__dict__.items()
                    if key in attrs}
