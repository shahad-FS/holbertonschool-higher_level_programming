#!/usr/bin/python3
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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if int(size) < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current square area"""
        return self.__size**2
