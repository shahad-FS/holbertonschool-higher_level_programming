#!/usr/bin/python3
"""Square Module"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """
        The __init__ method initialize instance variable

        Attributes:
        size : size of a square Private instance attribute
        """
        self.__size = size

    @property
    def size(self):
        """Getter to retrieve square size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter to set square size"""
        if not instance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area"""
        return self.__size**2
