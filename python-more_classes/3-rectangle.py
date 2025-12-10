#!/usr/bin/python3
"""Module for Rectangle class."""


class Rectangle:
    """Class representing a rectangle."""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter."""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter."""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """string representation of the rectangle using '#' characters."""
        if self.width == 0 or self.height == 0:
            return ""
        rect = ""
        for i in range(self.height):
            rect += "#" * self.width
            if i != self.height - 1:
                rect += "\n"
        return rect
