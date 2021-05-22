#!/usr/bin/python3
"""
This function indents the text variable

Arg:
    text (str): Text to be indented

Return:
    Nothing, just prints the indented text
"""


def text_indentation(text):
    """Function that prints an indented text"""

    space = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for character in text:
        if character == '.' or character == '?' or character == ':':
            space = 1
            print("{:s}".format(character))
            print()
        else:
            if space != 1:
                print("{:s}".format(character), end="")
            space = 0
    print()
