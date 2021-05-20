#!/usr/bin/python3
"""This is the class Square"""


class Square:
    """Coordinates of a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize variables"""

        self.size = size
        self.position = position

    def area(self):
        """Compute the area size of a square"""

        return self.__size ** 2

    @property
    def size(self):
        """Setter: Retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Getter: Set and verify the size"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
                raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Setter: Retrieve position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Getter: Set and verify the position"""

        if (not isinstance(value, tuple)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (not isinstance(value[0], int)) or (not isinstance(value[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Print the square"""

        position_y = self.__position[1]
        if self.__size != 0:
            for i in range(self.__size):
                for i in range(position_y):
                    print()
                    position_y -= 1
                for i in range(self.__position[0]):
                    print(" ", end="")
                for i in range(self.__size):
                    print("#", end="")
                if i != self.__size:
                    print()
        else:
            print()
