#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for rows in matrix:
            for cols in range(len(rows)):
                print("{:d}".format(rows[cols]), end="")
                if cols != len(rows) - 1:
                    print(end=" ")
            print()
