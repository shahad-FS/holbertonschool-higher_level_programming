#!/usr/bin/python3
"""Square Module"""


class Square:
    """Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """
        The __init__ method initialize instance variable

        Attributes:
        size : size of a square
        position : position of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter to retrieve square size"""
        return self.__size

    @property
    def position(self):
        """Getter to retrieve square position"""
        return self.__position

    @size.setter
    def size(self, value):
        """Setter to set square size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """Setter to set square position"""
        if not (isinstance(value, tuple) and len(value) == 2 and
                all(isinstance(num, int) for num in value) and
                all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area"""
        return self.__size**2

    def my_print(self):
        """print in stdout the square with the character #"""
        if self.size == 0:
            print()
        else:
            print("\n" * self.__position[1], end='')
            for row in range(self.__size):
                print(self.__position[0] * " " + self.size * "#")
