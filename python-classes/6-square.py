#!/usr/bin/python3
"""Square Module"""


class Square:
    """Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """
        The __init__ method initialize instance variable

        Attributes:
        size : size of a square Private instance attribute
        position : position of the square 
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
        self.__position = position
    @property
    def size(self):
        """Getter to retrieve square size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter to set square size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    @property
    def position(self):
        """Getter to retrieve square position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter to set square position"""
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    def area(self):
        """Return the current square area"""
        return self.__size**2
    def my_print(self):
        """print in stdout the square with the character #"""
        if self.__size == 0:
            print("")
            return
        else:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
        print("")
