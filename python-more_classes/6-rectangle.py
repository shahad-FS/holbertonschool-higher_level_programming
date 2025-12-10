#!/usr/bin/python3
"""Module for Rectangle class."""


class Rectangle:
    """Class representing a rectangle."""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize rectangle with width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __repr__(self):
        """official string representation of the rectangle."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """prints a message when an instance is deleted."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
        del self
