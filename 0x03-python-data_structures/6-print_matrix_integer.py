#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for r in range(0, len(matrix)):
        for c in range(0, len(matrix[r])):
            if c != 0:
                print(' ', end='')
            print("{:d}".format(matrix[r][c]), end='')
        print()
