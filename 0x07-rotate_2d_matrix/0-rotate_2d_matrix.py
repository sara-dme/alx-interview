#!/usr/bin/python3
"""Module doc"""


def rotate_2d_matrix(matrix):
    """ Given an n x n 2D matrix, rotate it 90 degrees clockwise"""
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
    for i in range(n):
        for j in range(int(n/2)):
            temp = matrix[i][n-j-1]
            matrix[i][n-j-1] = matrix[i][j]
            matrix[i][j] = temp
