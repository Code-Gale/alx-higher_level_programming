#!/usr/bin/python
def square_matrix_simple(matrix=[]):
    if not matrix:
        return
    return[[num * num for num in i] for i in matrix]
