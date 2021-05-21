#!/usr/bin/python3
"""
Function that make an integer addition

Verifies if it is an integer and if float,
converts it to integer
"""
def add_integer(a, b=98):
    """Function that adds 2 integers"""

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
