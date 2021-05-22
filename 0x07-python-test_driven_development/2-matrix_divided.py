#!/usr/bin/python3
"""
Function that divides all elements of a matrix and returns a new function

Args:
    matrix (list): Matrix to be divided
    div (float): Number to be use to divide

Return:
    New divided matrix
"""


def matrix_divided(matrix, div):
    """Function to divide a matrix by div"""

    result = []

    if matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if int(div) == 0:
        raise ZeroDivisionError("division by zero")

    idx = 0
    for col in matrix:
        sub_res = []
        for row in col:

            if not isinstance(row, int) and not isinstance(row, float):
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

            sub_res.append(round(row / div, 2))

        if len(sub_res) != len(matrix[idx]):
            raise TypeError("Each row of the matrix must have the same size")

        result.append(sub_res)

    return result
