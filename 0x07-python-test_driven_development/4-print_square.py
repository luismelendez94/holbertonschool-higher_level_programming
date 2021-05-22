#!/usr/bin/python3
"""
Function that prints a square with the character '#'

Arg:
    size (int): The length of the square

Return:
    Nothing, just prints a square
"""


def print_square(size):
    """Function to print a square"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for col in range(0, size):
        for row in range(0, size):
            print("#", end="")
        print()
