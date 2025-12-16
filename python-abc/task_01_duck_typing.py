#!/usr/bin/python3
"""Module for abstract base class for shapes"""
from abc import ABC, abstractmethod
from math import pi



class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Concrete class for Circle that inherits from Shape."""

    def __init__(self, radius):
        self.radius = abs(radius)

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius


class Rectangle(Shape):
    """Concrete class for Rectangle that inherits from Shape>"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Function to print area and perimeter of a shape."""

    area = shape.area()
    perimeter = shape.perimeter()

    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
