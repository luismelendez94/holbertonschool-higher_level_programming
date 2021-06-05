#!/usr/bin/python3
""" Pascal Triangle in a list of lists """


def pascal_triangle(n):
    """ Returns a list of lists representing the Pascal's Triangle of n """

    pascalList = list()

    if n <= 0:
        return pascalList

    for i in range(1, n+1):
        row = []
        C = 1
        for j in range(1, i+1):
            row.append(C)

            C = C * (i - j) // j
        pascalList.append(row)
    return pascalList
