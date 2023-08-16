#!/usr/bin/python
def square_matrix_simple(matrix=[]):
    updated_matrix = []
    for row in matrix:
        new_row = []
        for value in row:
            new_row.append(num ** 2)
        new_matrix.append(new_row)
    return new_matrix
