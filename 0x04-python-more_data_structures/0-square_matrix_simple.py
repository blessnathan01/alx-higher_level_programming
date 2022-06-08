#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    len_matrix = len(matrix)
    matrix2 = [[0 for x in range(len(matrix[0]))] for x in range(len_matrix)]
    for y in range(len_matrix):
        for z in range(len(matrix[y])):
            matrix2[y][z] = matrix[y][z] ** 2
    return matrix2
