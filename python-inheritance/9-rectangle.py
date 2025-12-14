#!/usr/bin/python3
"""Module contains class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Initialize width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """public instance method that returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """return the rectangle description"""
        return f"[Rectangle] {self.__width}/{self.__height}"
