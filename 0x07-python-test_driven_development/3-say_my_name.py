#!/usr/bin/python3
"""
Function that says my name
Verify if both variables are string and prints them

Args:
    first_name (str): The first parameter
    last_name (str): The second parameter

Returns:
    Nothings, the function prints something
"""

def say_my_name(first_name, last_name=""):
    """Function that prints the name pass"""

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
