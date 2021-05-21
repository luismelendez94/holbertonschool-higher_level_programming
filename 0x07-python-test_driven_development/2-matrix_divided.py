#!/usr/bin/python3
def matrix_divided(matrix, div):

    column = 0
    result = []

    if not isinstance(div, int) or not isinstance(div, float):
        raise TypeError("div must be a number")
    if div = 0:
        raise ZeroDivisionError("div must be a number")

    for col in matrix:
        for row in col:
            if not isinstance(matrix[col][row], int) and not isinstance(matrix[col][row]):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            count += 1
            result[col][row] = round(matrix[col][row] / div, 2)
        if count != len():
            raise TypeError("Each row of the matrix must have the same size")
