#!/usr/bin/python3
from abc import ABC, abstractmethod
"""Module for abstract base class for shapes"""


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
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14159 * self.radius


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
